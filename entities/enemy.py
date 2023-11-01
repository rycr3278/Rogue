import pygame as py
import config.settings as s
from ui.map import FLOOR, WALL, MAP_HEIGHT, MAP_WIDTH
import random

# enemy.py
from config.globals import enemy_group

class Enemy(py.sprite.Sprite):
    _instance = None
    
    @classmethod
    def get_instance(cls, dungeon_instance=None, x=None, y=None):
        if cls._instance is None or (x is not None and y is not None):
            cls._instance = Enemy(dungeon_instance, x, y)
        return cls._instance
    
    def __init__(self, dungeon_instance, pos_x=None, pos_y=None):
        super().__init__()
        self.dungeon_instance = dungeon_instance
        self.sprites_right = [
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
        self.sprites_left = [
            py.transform.flip(py.transform.scale(py.image.load(
                'Assets/Art/enemy1/1.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)), True, False),
            py.transform.flip(py.transform.scale(py.image.load(
                'Assets/Art/enemy1/2.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)), True, False),
            py.transform.flip(py.transform.scale(py.image.load(
                'Assets/Art/enemy1/3.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)), True, False),
            py.transform.flip(py.transform.scale(py.image.load(
                'Assets/Art/enemy1/4.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)), True, False),
            py.transform.flip(py.transform.scale(py.image.load(
                'Assets/Art/enemy1/5.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)), True, False),
            py.transform.flip(py.transform.scale(py.image.load(
                'Assets/Art/enemy1/6.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)), True, False),
            py.transform.flip(py.transform.scale(py.image.load(
                'Assets/Art/enemy1/7.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)), True, False),
            py.transform.flip(py.transform.scale(py.image.load(
                'Assets/Art/enemy1/8.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)), True, False),
            py.transform.flip(py.transform.scale(py.image.load(
                'Assets/Art/enemy1/9.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)), True, False)
        ]
        
        self.current_sprites = self.sprites_right
        self.current_sprite = 0
        self.image = self.current_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        
        self.move_counter = 0
        self.move_direction = random.randint(1,4)        
        
        if pos_x is None or pos_y is None or dungeon_instance.dungeon_map[pos_x][pos_y] != FLOOR:
            pos_x, pos_y = self.find_floor_tile(dungeon_instance)
    
        self.rect.topleft = [pos_x * s.TILE_SIZE, pos_y * s.TILE_SIZE]
    
    def is_wall_rect(self, rect):
        if not self.dungeon_instance or not hasattr(self.dungeon_instance, 'dungeon_map'):
            return False
        # Loop through each tile inside the rect's boundary
        for y in range(rect.top // s.TILE_SIZE, (rect.bottom + s.TILE_SIZE - 1) // s.TILE_SIZE):
            for x in range(rect.left // s.TILE_SIZE, (rect.right + s.TILE_SIZE - 1) // s.TILE_SIZE):
                x = max(0, min(x, len(self.dungeon_instance.dungeon_map) - 1))
                y = max(0, min(y, len(self.dungeon_instance.dungeon_map[0]) - 1))

                if self.dungeon_instance.dungeon_map[x][y] == WALL:
                    return True
        return False
    
    def handle_movement(self):
        dx = 0
        dy = 0
        
        if self.move_counter <= 0:
            self.move_direction = random.randint(1,4)
            self.move_counter = random.randint(50, 200)  # Decide new direction after 50 to 200 frames
        
        if self.move_direction == 1:  # left
            dx -= s.ENEMY_VEL
        elif self.move_direction == 2:  # right
            dx += s.ENEMY_VEL
        elif self.move_direction == 3:  # up
            dy -= s.ENEMY_VEL
        elif self.move_direction == 4:  # down
            dy += s.ENEMY_VEL

        # Predicted new rect after movement
        new_rect = self.rect.move(dx, dy)

        # Check for collisions
        if not self.is_wall_rect(new_rect):
            self.rect = new_rect
                
            # Determine animation based on direction
            if dx < 0:
                self.current_sprites = self.sprites_left
                self.direction = 'left'
                self.is_animating = True
            elif dx > 0:
                self.current_sprites = self.sprites_right
                self.direction = 'right'
                self.is_animating = True
            if dy < 0:
                self.current_sprites = self.sprites_left
                self.direction = 'up'
                self.is_animating = True
            elif dy > 0:
                self.current_sprites = self.sprites_right
                self.direction = 'down'
                self.is_animating = True
                    
        self.move_counter -= 1
        
    def find_floor_tile(self, dungeon_instance):
        """Find a random floor tile to place the enemy."""
        while True:
            x = random.randint(0, MAP_WIDTH - 1)
            y = random.randint(0, MAP_HEIGHT - 1)

            if dungeon_instance.dungeon_map[x][y] == FLOOR:
                return x, y
    
    def animate(self):
        self.is_animating = True
    
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2
        
        if self.current_sprite >= len(self.current_sprites):
            self.current_sprite = 0
            #self.is_animating = False
        
        self.image = self.current_sprites[int(self.current_sprite)]
        
