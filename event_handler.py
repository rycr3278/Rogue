import pygame as py
from entities.item import Item

def handle_events(cursor, item_group):
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            return False  # Signal to end the game loop in main.py

        if event.type == py.MOUSEBUTTONDOWN:
            cursor_clicked_item = cursor.mouseClick()
            if cursor_clicked_item:
                cursor.channel.play(cursor.click)
                for item in py.sprite.spritecollide(cursor, item_group, False):
                    item_group.remove(item)

    return True  # Signal to continue the game loop in main.py
