import pygame as py
import config.settings as settings
from entities.player import Player1
from entities.enemy import Enemy, enemy_group
from entities.item import Item
from ui.cursor import Cursor, cursor_group

# initialize pygame modules
py.init()
py.font.init()
py.mixer.init()

def draw_window(player1, item_group, cursor):
    settings.WIN.blit(settings.BG, (0, 0))
    
    item_group.draw(settings.WIN)
    item_group.update()
    
    enemy_group.draw(settings.WIN)
    enemy_group.update()
    
    cursor_group.draw(settings.WIN)
    cursor_group.update()
    
    py.draw.rect(settings.WIN, (255, 0, 0), cursor.rect, 2)  # Draw cursor rect in red
    for item in item_group:
        py.draw.rect(settings.WIN, (0, 255, 0), item.rect, 2)  # Draw item rects in green
    
    settings.WIN.blit(player1.image, (player1.rect.x, player1.rect.y))  # Use player1's image
    py.display.update()

def main():
    py.mouse.set_visible(False)
    player1 = Player1()
    player1.rect.x = settings.WIDTH // 2
    player1.rect.y = settings.HEIGHT - 100
    player_group = py.sprite.Group()
    player_group.add(player1)

    cursor = Cursor.get_instance()
    enemy = Enemy.get_group()
    item_group = Item.get_group()

    clock = py.time.Clock()
    run = True
    while run:
        clock.tick(settings.FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                py.quit()
                return  # This will exit the main() function immediately

            if event.type == py.MOUSEBUTTONDOWN:                
                cursor_clicked_item = cursor.mouseClick()
                if cursor_clicked_item:
                    cursor.channel.play(cursor.click)  # Play the click sound here
                    for item in py.sprite.spritecollide(cursor, item_group, False): 
                        # Handle any other logic when an item is clicked
                        item_group.remove(item)

            if event.type == py.KEYDOWN:
                for e in enemy:
                    e.animate()
        cursor.update()
        keys_pressed = py.key.get_pressed()
        player1.handle_movement(keys_pressed)        
        draw_window(player1, item_group, cursor)
        player_group.update()
    print(f"Number of sprites in cursor_group: {len(cursor_group)}")

# entry point
if __name__ == "__main__":
    main()
