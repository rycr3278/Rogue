import pygame as py
import config.settings as settings
from entities.player import Player1
from entities.enemy import Enemy
from entities.item import Item
from ui.cursor import Cursor, cursor_group
from draw import draw_window  

# initialize pygame modules
py.init()
py.font.init()
py.mixer.init()



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
