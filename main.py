import pygame as py
import config.settings as settings
from entities.player import Player1
from entities.enemy import Enemy
from entities.item import Item
from ui.cursor import Cursor, cursor_group
from draw import draw_window
from event_handler import handle_events
from ui.map import DungeonMap, MAP_HEIGHT, MAP_WIDTH, FLOOR, DOOR, USED_DOOR
from config.globals import enemy_group, item_group

# Initialize pygame modules needed for the game
py.init()
py.font.init()
py.mixer.init()

# Create an instance of the dungeon map
dungeon = DungeonMap()

# Wipe settings
WIPE_SPEED = 60  # adjust for speed

# Black rectangle for wiping
wipe_rect = py.Rect(0, 0, 0, settings.HEIGHT)
is_wiping = False
wiping_direction = 1  # 1 for wiping in, -1 for wiping out



# Get the player instance and set its position
player1 = Player1.get_instance(dungeon)
# Loop through the dungeon map to find a floor tile to position the player
for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        if dungeon.dungeon_map[x][y] == FLOOR:
            player1.rect.x = x * settings.TILE_SIZE
            player1.rect.y = y * settings.TILE_SIZE
            break
    else:
        continue
    break


def get_new_spawn_coordinates(direction, new_dungeon):
    door_coords = new_dungeon.get_door_coordinates()
    print('door coords', door_coords)

    # Determine the opposite door direction
    opposite_direction = {
        "left": "right",
        "right": "left",
        "top": "bottom",
        "bottom": "top"
    }.get(direction)
    print('player should appear on the door tile at the ', opposite_direction, ' of the new room')
    
    if opposite_direction in door_coords:  # Additional check to ensure the key exists
        x, y = door_coords[opposite_direction]
        
        # Ensure x and y are within valid range
        x = max(0, min(x, MAP_WIDTH * settings.TILE_SIZE - 1))
        y = max(0, min(y, MAP_HEIGHT * settings.TILE_SIZE - 1))
        print('get_new_spawn_coordinates is outputting coordinates: x:', x, ', y:', y)
        return x, y
    else:
        print("Unexpected door_direction:", direction)
        # Return default spawn location (center of the map)
        return MAP_WIDTH * settings.TILE_SIZE // 2, MAP_HEIGHT * settings.TILE_SIZE // 2



# Main game loop function
def main():
    # Hide the default mouse cursor
    py.mouse.set_visible(False)
    
    # Declare global wipe variables
    global player1, is_wiping, wiping_direction, wipe_rect, dungeon
    
    # Create a sprite group for the player
    player_group = py.sprite.Group()
    player_group.add(player1)

    # Get the cursor instance
    cursor = Cursor.get_instance()
    
    # Create an enemy instance and add it to the enemy group
    enemy = Enemy(dungeon)
    enemy_group.add(enemy)
    enemy.animate()
    
    # Create an item instance and add it to the item group
    item = Item(dungeon, 'Assets/Art/orb_red.png')
    item_group.add(item)

    # Initialize game clock to regulate FPS
    clock = py.time.Clock()
    run = True  
    
    # Main game loop
    while run:
        # Handle all game events (like input)
        run = handle_events(cursor, item_group)
        
        # If the game should quit, break out of the loop
        if not run:
            break
        
        # Update game state every frame according to the set FPS
        clock.tick(settings.FPS)
        cursor.update()
        keys_pressed = py.key.get_pressed()
        player1.handle_movement(keys_pressed)
        
        # Render the game scene
        dungeon.display_map(settings.WIN)        
        draw_window(player1, item_group, cursor)

        # Check for door collisions
        door_direction = player1.collided_with_door()
        
        if door_direction and not is_wiping:
            
            print('player walked through the door at the ', door_direction)
            
            # Generate new map
            new_dungeon = DungeonMap()
            
            # Determine the new spawn coordinates based on the door's direction
            new_x, new_y = get_new_spawn_coordinates(door_direction, new_dungeon)
            
            print("new_x, new_y", new_x, new_y)
            
            # shut door
            new_dungeon.dungeon_map[new_x][new_y] = USED_DOOR
            
            if new_x is not None and new_y is not None:
                
                is_wiping = True
                wiping_direction = 1  # Start the wipe-in transition
            else:
                print("Failed to get new spawn coordinates.")
            
        if is_wiping:
            if wiping_direction == 1:  # Wiping in
                if wipe_rect.width < settings.WIDTH:
                    wipe_rect.width += WIPE_SPEED
                else:
                    # Switch to the new dungeon
                    dungeon = new_dungeon
                    
                    # Remove the current player instance
                    player1.remove()

                    # For rendering
                    render_x = new_x * settings.TILE_SIZE
                    render_y = new_y * settings.TILE_SIZE
                    
                    # offset player position to help prevent spawning in walls
                    if door_direction == "top":
                        render_y -= settings.PLAYER1_HEIGHT
                    elif door_direction == "bottom":
                        render_y += settings.PLAYER1_HEIGHT
                    elif door_direction == "left":
                        render_x -= settings.PLAYER1_WIDTH * 2
                    elif door_direction == "right":
                        render_x += settings.PLAYER1_WIDTH

                    # Create a new player instance at the new coordinates
                    player1 = Player1.get_instance(dungeon, render_x, render_y)
                    print('player generated at render_x: ', render_x, ' and render_y: ', render_y)

                    player_group.add(player1)  # Add the new player instance to the sprite group

                    wiping_direction = -1  # Start wiping out

            elif wiping_direction == -1:  # Wiping out
                if wipe_rect.width > 0:
                    wipe_rect.width -= WIPE_SPEED
                else:
                    is_wiping = False  # End the wipe effect

            # Render the wipe effect on top of the game scene
            settings.WIN.fill((0,0,0), wipe_rect)

        # Update the screen
        py.display.flip()

        # Update the player's state
        player_group.update()
       

# If this script is the main script being run, start the game
if __name__ == "__main__":
    main()

