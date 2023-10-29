import pygame as py
import config.settings as s



class Player1(py.sprite.Sprite):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Player1('Assets/Art/player1/axe_shield/walk_down/tile180.png')
        return cls._instance
    
    def __init__(self):
        super().__init__()
        
        # player walking
        self.sprites_down = [
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile180.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile181.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile182.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile183.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile184.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile185.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile186.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile187.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile188.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        ]
        self.sprites_left = [
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile162.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile163.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile164.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile165.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile166.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile167.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile168.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile169.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile170.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        ]
        self.sprites_right = [
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile198.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile199.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile200.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile201.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile202.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile203.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile204.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile205.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile206.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        ]
        self.sprites_up = [ 
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile144.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile145.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile146.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile147.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile148.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile149.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile150.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile151.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile152.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)),
        ]
        
        
        self.current_sprite = 0
        
        self.current_sprites = self.sprites_down
        self.current_sprite = 0
        self.image = self.current_sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        
        self.is_animating = False
        
        self.direction = "down" # default direction
        
    def animate(self):
        self.is_animating = True
    
    def update(self):
        if self.is_animating:
            self.current_sprite += 0.2    
            if self.current_sprite >= len(self.current_sprites):  # Use current_sprites instead of sprites
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.current_sprites[int(self.current_sprite)]
    
    def handle_movement(self, keys_pressed):
        self.is_animating = False
        
        if keys_pressed[py.K_a] and self.rect.x - s.VEL > 0: # left
            self.rect.x -= s.VEL
            self.current_sprites = self.sprites_left
            self.direction = 'left'
            self.is_animating = True
        if keys_pressed[py.K_d] and self.rect.x + s.VEL + s.PLAYER1_WIDTH < s.WIDTH: # right
            self.rect.x += s.VEL
            self.current_sprites = self.sprites_right
            self.direction = 'right'
            self.is_animating = True
        if keys_pressed[py.K_w] and self.rect.y - s.VEL > 0: # up
            self.rect.y -= s.VEL
            self.current_sprites = self.sprites_up
            self.direction = 'up'
            self.is_animating = True
        if keys_pressed[py.K_s] and self.rect.y + s.VEL  + s.PLAYER1_HEIGHT < s.HEIGHT: # down
            self.rect.y += s.VEL
            self.current_sprites = self.sprites_down
            self.direction = 'down'
            self.is_animating = True