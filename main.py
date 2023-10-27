import pygame as py
import os
import settings as s
import random

# initialize pygame modules
py.init()
py.font.init()
py.mixer.init()

# classes
class Cursor(py.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = py.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.channel = py.mixer.Channel(0)
        self.click = py.mixer.Sound('Assets/Sound/mixkit-classic-click-1117.wav')
        
    def mouseClick(self):
        items_hit = py.sprite.spritecollide(self, item_group, False)
        if items_hit:
            self.channel.play(self.click)
            return True
        return False

    def update(self):
        self.rect.x, self.rect.y = py.mouse.get_pos()


class Player1(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites_down = []
        self.sprites_left = []
        self.sprites_right = []
        self.sprites_up = []
        
        self.sprites_down.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile180.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_down.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile181.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_down.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile182.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_down.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile183.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_down.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile184.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_down.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile185.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_down.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile186.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_down.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile187.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_down.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_down/tile188.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        
        self.sprites_left.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile162.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_left.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile163.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_left.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile164.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_left.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile165.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_left.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile166.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_left.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile167.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_left.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile168.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_left.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile169.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_left.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_left/tile170.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        
        self.sprites_right.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile198.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_right.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile199.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_right.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile200.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_right.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile201.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_right.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile202.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_right.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile203.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_right.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile204.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_right.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile205.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_right.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_right/tile206.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        
        self.sprites_up.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile144.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_up.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile145.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_up.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile146.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_up.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile147.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_up.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile148.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_up.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile149.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_up.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile150.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_up.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile151.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
        self.sprites_up.append(py.transform.scale(py.image.load('Assets/Art/player1/axe_shield/walk_up/tile152.png'), (s.PLAYER1_WIDTH, s.PLAYER1_HEIGHT)))
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
    
    def handle_movement(keys_pressed, player1):
        if keys_pressed[py.K_a] and player1.rect.x - s.VEL > 0: # left
            player1.rect.x -= s.VEL
            player1.current_sprites = player1.sprites_left
            player1.direction = 'left'
            player1.animate()
        if keys_pressed[py.K_d] and player1.rect.x + s.VEL + s.PLAYER1_WIDTH < WIDTH: # right
            player1.rect.x += s.VEL
            player1.current_sprites = player1.sprites_right
            player1.direction = 'right'
            player1.animate()
        if keys_pressed[py.K_w] and player1.rect.y - s.VEL > 0: # up
            player1.rect.y -= s.VEL
            player1.current_sprites = player1.sprites_up
            player1.direction = 'up'
            player1.animate()
        if keys_pressed[py.K_s] and player1.rect.y + s.VEL  + s.PLAYER1_HEIGHT < HEIGHT: # down
            player1.rect.y += s.VEL
            player1.current_sprites = player1.sprites_down
            player1.direction = 'down'
            player1.animate()
        
class Item(py.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = py.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class Enemy(py.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(py.transform.scale(py.image.load('Assets/Art/enemy1/1.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)))
        self.sprites.append(py.transform.scale(py.image.load('Assets/Art/enemy1/2.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)))
        self.sprites.append(py.transform.scale(py.image.load('Assets/Art/enemy1/3.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)))
        self.sprites.append(py.transform.scale(py.image.load('Assets/Art/enemy1/4.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)))
        self.sprites.append(py.transform.scale(py.image.load('Assets/Art/enemy1/5.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)))
        self.sprites.append(py.transform.scale(py.image.load('Assets/Art/enemy1/6.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)))
        self.sprites.append(py.transform.scale(py.image.load('Assets/Art/enemy1/7.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)))
        self.sprites.append(py.transform.scale(py.image.load('Assets/Art/enemy1/8.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)))
        self.sprites.append(py.transform.scale(py.image.load('Assets/Art/enemy1/9.png'), (s.ENEMY_WIDTH, s.ENEMY_HEIGHT)))
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
            self.is_animating = False
        
        self.image = self.sprites[int(self.current_sprite)]
        

# window
WIDTH, HEIGHT = 1200, 900
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Veiled Hollow")
py.mouse.set_visible(False)

# constant colors
DARK_BLUE = (62, 76, 89)
MED_BLUE = (128, 167, 191)
LIGHT_BLUE = (172, 215, 242)

YELLOW = (242, 220, 153)

BROWN = (191, 131, 78)

BG = py.image.load(os.path.join('Assets/Art/workingbg.jpg'))

# enemy
enemy_group = py.sprite.Group()
enemy = Enemy(100, 100)
enemy_group.add(enemy)

# player images
player1_SPRITE = py.image.load(os.path.join('Assets/Art/Body.png'))

# draw game window
def draw_window(player1):
    WIN.blit(BG, (0, 0))
    
    item_group.draw(WIN)
    item_group.update()
    
    enemy_group.draw(WIN)
    enemy_group.update()
    
    cursor_group.draw(WIN)
    cursor_group.update()
    
    WIN.blit(player1.image, (player1.rect.x, player1.rect.y))  # Use player1's image
    
    py.display.update()
    
# cursor
cursor = Cursor('Assets/Art/Cursor1.png')
cursor_group = py.sprite.Group()
cursor_group.add(cursor)

# item
item_group = py.sprite.Group()
new_item = Item('Assets/Art/orb_red.png', WIDTH // 2, HEIGHT // 2)
item_group.add(new_item)


def main():
    player1 = Player1()
    player1.rect.x = WIDTH // 2
    player1.rect.y = HEIGHT - 100
    player_group = py.sprite.Group()
    player_group.add(player1)
    
    clock = py.time.Clock()
    run = True
    while run:
        clock.tick(s.FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                py.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                cursor_clicked_item = cursor.mouseClick()
                if cursor_clicked_item:
                    for item in py.sprite.spritecollide(cursor, item_group, True):
                    # Handle any other logic when an item is clicked
                        pass
            if event.type == py.KEYDOWN:
                enemy.animate()
                


        keys_pressed = py.key.get_pressed()
        Player1.handle_movement(keys_pressed, player1)        
        
        draw_window(player1)
        player_group.update()


# entry point
if __name__ == "__main__":
    main()