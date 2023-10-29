import pygame as py
import config.settings as s

class Item(py.sprite.Sprite):
    _group = py.sprite.Group()

    @classmethod
    def get_group(cls):
        return cls._group
    
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = py.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self._group.add(self)  # Automatically add the item instance to the group
        print(f"Item positioned at: ({pos_x}, {pos_y})")  # Diagnostic print
        print(f"Item rect size: {self.rect.width}x{self.rect.height}")  # Diagnostic print


# item
new_item = Item('Assets/Art/orb_red.png', s.WIDTH // 2, s.HEIGHT // 2)
