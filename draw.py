import pygame as py
import config.settings as settings
from entities.enemy import enemy_group
from ui.cursor import cursor_group

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
        
    for enemy in enemy_group:
        py.draw.rect(settings.WIN, (0, 0, 255), enemy.rect, 2) # Draw enemy rects in blue
        
    
    settings.WIN.blit(player1.image, (player1.rect.x, player1.rect.y))  # Use player1's image
    py.draw.rect(settings.WIN, (255, 255, 255), player1.rect, 2) # Draw player rect in white
    
    py.display.update()