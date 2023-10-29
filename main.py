import pygame as py
import config.settings as settings
from entities.player import Player1
from entities.enemy import Enemy
from entities.item import Item
from ui.cursor import Cursor, cursor_group
from draw import draw_window
from event_handler import handle_events

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
        run = handle_events(cursor, item_group)
        cursor.update()
        keys_pressed = py.key.get_pressed()
        player1.handle_movement(keys_pressed)        
        draw_window(player1, item_group, cursor)
        player_group.update()
    print(f"Number of sprites in cursor_group: {len(cursor_group)}")

# entry point
if __name__ == "__main__":
    main()
