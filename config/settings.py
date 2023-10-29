import pygame as py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ui.map import DungeonMap, MAP_WIDTH, MAP_HEIGHT, FLOOR, WALL

# constant colors
DARK_BLUE = (62, 76, 89)
MED_BLUE = (128, 167, 191)
LIGHT_BLUE = (172, 215, 242)
YELLOW = (242, 220, 153)
BROWN = (191, 131, 78)

# Constants for display
TILE_SIZE = 40  # Size of each cell in pixels
WIDTH = MAP_WIDTH * TILE_SIZE
HEIGHT = MAP_HEIGHT * TILE_SIZE
FLOOR_TILE = py.image.load(os.path.join('Assets/Art/map_tiles/tile009.png'))
FLOOR_TILE = py.transform.scale(FLOOR_TILE, (TILE_SIZE, TILE_SIZE))

WALL_TILE =  py.image.load(os.path.join('Assets/Art/map_tiles/tile012.png')) 
WALL_TILE = py.transform.scale(WALL_TILE, (TILE_SIZE, TILE_SIZE))

# game settings
FPS = 60
VEL = 2

PLAYER1_WIDTH, PLAYER1_HEIGHT = 60, 60

ENEMY_WIDTH, ENEMY_HEIGHT = 32, 48

# window
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Veiled Hollow")
py.mouse.set_visible(False)


BG = py.image.load(os.path.join('Assets/Art/workingbg.jpg'))