import pygame as py
import config.settings as s
from ui.map import DungeonMap, FLOOR
import random

# enemy.py
from config.globals import enemy_group


class Enemy(py.sprite.Sprite):
    
    def __init__(self, dungeon_map, pos_x=None, pos_y=None):
        super().__init__()
        self.sprites = [
            py.transform.scale(py.image.load('Assets/Art/enemy1/1.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)),
            py.transform.scale(py.image.load('Assets/Art/enemy1/2.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)),
            py.transform.scale(py.image.load('Assets/Art/enemy1/3.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)),
            py.transform.scale(py.image.load('Assets/Art/enemy1/4.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)),
            py.transform.scale(py.image.load('Assets/Art/enemy1/5.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)),
            py.transform.scale(py.image.load('Assets/Art/enemy1/6.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)),
            py.transform.scale(py.image.load('Assets/Art/enemy1/7.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)),
            py.transform.scale(py.image.load('Assets/Art/enemy1/8.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)),
            py.transform.scale(py.image.load('Assets/Art/enemy1/9.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT))
        ]
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        
        self.rect = self.image.get_rect()        
        
        if pos_x is None or pos_y is None or dungeon_map[pos_x][pos_y] != FLOOR:
            pos_x, pos_y = self.find_floor_tile(dungeon_map)
    
        self.rect.topleft = [pos_x * s.TILE_SIZE, pos_y * s.TILE_SIZE]
        
        
    def find_floor_tile(self, dungeon_map):
        """Find a random floor tile to place the enemy."""
        while True:
            x = random.randint(0, len(dungeon_map.dungeon_map) - 1)
            y = random.randint(0, len(dungeon_map.dungeon_map[0]) - 1)

            if dungeon_map.dungeon_map[x][y] == FLOOR:
                return x, y
    
    def animate(self):
        self.is_animating = True
    
        
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            #self.is_animating = False
        
        self.image = self.sprites[int(self.current_sprite)]
        
