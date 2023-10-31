import pygame as py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ui.map import MAP_WIDTH, MAP_HEIGHT

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

DEFAULT_TILE = FLOOR_TILE

WALL_TILE =  py.image.load(os.path.join('Assets/Art/map_tiles/tile012.png')) 
WALL_TILE = py.transform.scale(WALL_TILE, (TILE_SIZE, TILE_SIZE))

TOP_EDGE_TILE =  py.image.load(os.path.join('Assets/Art/map_tiles/tile019.png')) 
TOP_EDGE_TILE = py.transform.scale(TOP_EDGE_TILE, (TILE_SIZE, TILE_SIZE))

RIGHT_EDGE_TILE =  py.image.load(os.path.join('Assets/Art/map_tiles/tile018.png')) 
RIGHT_EDGE_TILE = py.transform.scale(RIGHT_EDGE_TILE, (TILE_SIZE, TILE_SIZE))

LEFT_EDGE_TILE =  py.image.load(os.path.join('Assets/Art/map_tiles/tile020.png')) 
LEFT_EDGE_TILE = py.transform.scale(LEFT_EDGE_TILE, (TILE_SIZE, TILE_SIZE))

LEFT_TOP_CORNER_TILE = py.image.load(os.path.join('Assets/Art/map_tiles/tile029.png'))
LEFT_TOP_CORNER_TILE = py.transform.scale(LEFT_TOP_CORNER_TILE, (TILE_SIZE, TILE_SIZE))

RIGHT_TOP_CORNER_TILE = py.image.load(os.path.join('Assets/Art/map_tiles/tile027.png'))
RIGHT_TOP_CORNER_TILE = py.transform.scale(RIGHT_TOP_CORNER_TILE, (TILE_SIZE, TILE_SIZE))

LEFT_BOTTOM_CORNER_TILE = py.image.load(os.path.join('Assets/Art/map_tiles/tile036.png'))
LEFT_BOTTOM_CORNER_TILE = py.transform.scale(LEFT_BOTTOM_CORNER_TILE, (TILE_SIZE, TILE_SIZE))

RIGHT_BOTTOM_CORNER_TILE = py.image.load(os.path.join('Assets/Art/map_tiles/tile038.png'))
RIGHT_BOTTOM_CORNER_TILE = py.transform.scale(RIGHT_BOTTOM_CORNER_TILE, (TILE_SIZE, TILE_SIZE))

BOTTOM_EDGE_TILE = py.transform.rotate(LEFT_EDGE_TILE, 90)

DOOR_TILE = py.image.load(os.path.join('Assets/Art/map_tiles/tile039.png'))
DOOR_TILE = py.transform.scale(DOOR_TILE, (TILE_SIZE, TILE_SIZE))

USED_DOOR_TILE = py.image.load(os.path.join('Assets/Art/map_tiles/tile041.png'))
USED_DOOR_TILE = py.transform.scale(USED_DOOR_TILE, (TILE_SIZE, TILE_SIZE))

# game settings
FPS = 60
VEL = 6

PLAYER1_WIDTH, PLAYER1_HEIGHT = 64, 64

ENEMY_WIDTH, ENEMY_HEIGHT = 32, 48

# window
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Veiled Hollow")
py.mouse.set_visible(False)
