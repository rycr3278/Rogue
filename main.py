import pygame as py
import config.settings as settings
from entities.player import Player1
from entities.enemy import Enemy
from entities.item import Item
from ui.cursor import Cursor, cursor_group
from draw import draw_window
from event_handler import handle_events
from ui.map import DungeonMap, MAP_HEIGHT, MAP_WIDTH, FLOOR, DOOR
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

    # Determine the opposite door direction
    opposite_direction = {
        "left": "right",
        "right": "left",
        "top": "bottom",
        "bottom": "top"
    }.get(direction)
    
    if opposite_direction in door_coords:  # Additional check to ensure the key exists
        x, y = door_coords[opposite_direction]
        if opposite_direction == "top":
            y += settings.TILE_SIZE
        elif opposite_direction == "bottom":
            y -= settings.TILE_SIZE
        elif opposite_direction == "left":
            x += settings.TILE_SIZE
        elif opposite_direction == "right":
            x -= settings.TILE_SIZE
        return x, y
    else:
        print("Unexpected door_direction:", direction)
        return None, None


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
            # Generate new map
            new_dungeon = DungeonMap()

            # Determine the new spawn coordinates based on the door's direction
            new_x, new_y = get_new_spawn_coordinates(door_direction, new_dungeon)
            print("new_x, new_y", new_x, new_y)
            
            if new_x is not None and new_y is not None:
                print(door_direction)
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

                    # Create a new player instance at the new coordinates
                    player1 = Player1.get_instance(dungeon, (new_x * settings.TILE_SIZE), (new_y * settings.TILE_SIZE))
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

