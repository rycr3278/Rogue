import pygame as py
from entities.item import Item

py.mixer.init()

class Cursor(py.sprite.Sprite):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Cursor('Assets/Art/Cursor1.png')
        return cls._instance
    
    def __init__(self, picture_path):
        print("Cursor instance created")
        super().__init__()
        self.image = py.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.channel = py.mixer.Channel(0)
        self.click = py.mixer.Sound('Assets/Sound/mixkit-classic-click-1117.wav')
        print(f"Cursor rect size: {self.rect.width}x{self.rect.height}")  # Diagnostic print

        
    def mouseClick(self):
        print("Checking for collision...")  # Diagnostic print
        print(f"Cursor checking collision at: ({self.rect.x}, {self.rect.y})")  # Diagnostic print
        for item in Item.get_group():
            print(f"Item at: ({item.rect.x}, {item.rect.y}) with size: {item.rect.width}x{item.rect.height}")
        print(f"Number of items: {len(Item.get_group())}")  # Diagnostic print
        items_hit = py.sprite.spritecollide(self, Item.get_group(), False)  # Don't remove the item here
        return bool(items_hit)


    def update(self):
        mouseX, mouseY = py.mouse.get_pos()
        self.rect.x = mouseX - self.rect.width // 2
        self.rect.y = mouseY - self.rect.height // 2
        self.rect.x, self.rect.y = py.mouse.get_pos()
        #print(f"Cursor positioned at: ({self.rect.x}, {self.rect.y})")  # Diagnostic print
        
# cursor
cursor = Cursor('Assets/Art/Cursor1.png')
cursor_group = py.sprite.Group()
cursor_group.add(cursor)