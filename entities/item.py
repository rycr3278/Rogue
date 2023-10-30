import pygame as py
import config.settings as s
import random
from ui.map import DungeonMap, FLOOR
from config.globals import item_group

class Item(py.sprite.Sprite):
    
    def __init__(self, dungeon_map, picture_path, pos_x=None, pos_y=None):
        super().__init__()
        self.image = py.image.load(picture_path)
        self.rect = self.image.get_rect()
        item_group.add(self)  # Automatically add the item instance to the group

        
        if pos_x is None or pos_y is None or dungeon_map[pos_x][pos_y] != FLOOR:
            pos_x, pos_y = self.find_floor_tile(dungeon_map)
    
        self.rect.topleft = [pos_x * s.TILE_SIZE, pos_y * s.TILE_SIZE]
        print(f"Item positioned at: ({pos_x}, {pos_y})")  # Diagnostic print
        print(f"Item rect size: {self.rect.width}x{self.rect.height}")  # Diagnostic print
        
    def find_floor_tile(self, dungeon_map):
        """Find a random floor tile to place the item."""
        while True:
            x = random.randint(0, len(dungeon_map.dungeon_map) - 1)
            y = random.randint(0, len(dungeon_map.dungeon_map[0]) - 1)

            if dungeon_map.dungeon_map[x][y] == FLOOR:
                return x, y


# item
#new_item = Item('Assets/Art/orb_red.png', s.WIDTH // 2, s.HEIGHT // 2)
