import pygame as py
import config.settings as s

class Enemy(py.sprite.Sprite):
    enemy_group = py.sprite.Group()  # Class-level attribute

    @classmethod
    def get_group(cls):
        return cls.enemy_group
    
    def __init__(self, pos_x, pos_y):
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
        self.rect.topleft = [pos_x, pos_y]
        
    
    def animate(self):
        self.is_animating = True
    
        
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            #self.is_animating = False
        
        self.image = self.sprites[int(self.current_sprite)]
        
# enemy
enemy_group = py.sprite.Group()
enemy = Enemy(100, 100)
enemy_group.add(enemy)
enemy.animate()