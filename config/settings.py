import pygame as py
import os

# game settings
FPS = 60
VEL = 2

PLAYER1_WIDTH, PLAYER1_HEIGHT = 60, 60

ENEMY_WIDTH, ENEMY_HEIGHT = 32, 48

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