import random
import pygame as py
import config.settings as settings


# Constants
FLOOR = 0
WALL = 1
DOOR = 2
TOP_EDGE = 3
RIGHT_EDGE = 4
LEFT_EDGE = 5

# Map dimensions
MAP_WIDTH = 48
MAP_HEIGHT = 27

class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def create_room(self, dungeon_map):
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.height):
                dungeon_map[x][y] = FLOOR
        print(f"Room created at x:{self.x}, y:{self.y}, width:{self.width}, height:{self.height}")

class DungeonMap:
    def __init__(self):
        self.dungeon_map = [[WALL for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
        self.rooms = []
        self.generate_dungeon()

    def add_room(self, room):
        # Check if room overlaps with existing rooms before adding.
        overlap = False
        for r in self.rooms:
            if (room.x < r.x + r.width and room.x + room.width > r.x and
                room.y < r.y + r.height and room.y + room.height > r.y):
                overlap = True
                break
        
        if not overlap:
            room.create_room(self.dungeon_map)
            self.rooms.append(room)

    def connect_rooms(self, room1, room2):
        # Find center of rooms
        x1, y1 = room1.x + room1.width // 2, room1.y + room1.height // 2
        x2, y2 = room2.x + room2.width // 2, room2.y + room2.height // 2

        # Randomly choose to start horizontal or vertical
        if random.randint(0, 1) == 1:
            # Move horizontally
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.dungeon_map[x][y1] = FLOOR
                if y1 + 2 < MAP_HEIGHT:  # Ensure we're not out of bounds
                    self.dungeon_map[x][y1 + 1] = FLOOR  # Add tile below for 2-tile-wide corridor
                    self.dungeon_map[x][y1 + 2] = FLOOR  # Add tile below for 3-tile-wide corridor
            # Then move vertically
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.dungeon_map[x2][y] = FLOOR
                if x2 + 1 < MAP_WIDTH:  # Ensure we're not out of bounds
                    self.dungeon_map[x2 + 1][y] = FLOOR  # Add tile to the right for 2-tile-wide corridor
                    self.dungeon_map[x2 + 2][y] = FLOOR  # Add tile to the right for 3-tile-wide corridor
        else:
            # Move vertically
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.dungeon_map[x1][y] = FLOOR
                if x1 + 1 < MAP_WIDTH:  # Ensure we're not out of bounds
                    self.dungeon_map[x1 + 1][y] = FLOOR  # Add tile to the right for 2-tile-wide corridor
                    self.dungeon_map[x1 + 2][y] = FLOOR  # Add tile to the right for 3-tile-wide corridor
            # Then move horizontally
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.dungeon_map[x][y2] = FLOOR
                if y2 + 1 < MAP_HEIGHT:  # Ensure we're not out of bounds
                    self.dungeon_map[x][y2 + 1] = FLOOR  # Add tile below for 2-tile-wide corridor
                    self.dungeon_map[x][y2 + 2] = FLOOR  # Add tile below for 3-tile-wide corridor

    def add_transitional_tiles(self):
        for y in range(1, MAP_HEIGHT - 1):
            for x in range(1, MAP_WIDTH - 1):
                if self.dungeon_map[x][y] == FLOOR:
                    top = self.dungeon_map[x][y-1]
                    right = self.dungeon_map[x+1][y]
                    left = self.dungeon_map[x-1][y]

                    # Check for top edge
                    if top == WALL:
                        self.dungeon_map[x][y] = TOP_EDGE
                    # Check for right edge
                    elif right == WALL:
                        self.dungeon_map[x][y] = RIGHT_EDGE
                    # Check for left edge
                    elif left == WALL:
                        self.dungeon_map[x][y] = LEFT_EDGE


    def generate_dungeon(self):
        # Generate multiple rooms and connect them
        for i in range(10):  # Example: 10 rooms
            room = Room(random.randint(0, MAP_WIDTH - 10), random.randint(0, MAP_HEIGHT - 10), random.randint(5, 10), random.randint(5, 10))
            self.add_room(room)
        print(f"Total rooms generated: {len(self.rooms)}")
        # Connect the rooms
        for i in range(len(self.rooms) - 1):
            self.connect_rooms(self.rooms[i], self.rooms[i + 1])
        self.add_transitional_tiles()

    def display_map(self, screen):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                screen.blit(settings.DEFAULT_TILE, (x * settings.TILE_SIZE, y * settings.TILE_SIZE))
                
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):        
                if self.dungeon_map[x][y] == FLOOR:
                    tile = settings.FLOOR_TILE
                elif self.dungeon_map[x][y] == TOP_EDGE:
                    tile = settings.TOP_EDGE_TILE
                elif self.dungeon_map[x][y] == RIGHT_EDGE:
                    tile = settings.RIGHT_EDGE_TILE
                elif self.dungeon_map[x][y] == LEFT_EDGE:
                    tile = settings.LEFT_EDGE_TILE
                else:
                    tile = settings.WALL_TILE
                screen.blit(tile, (x*settings.TILE_SIZE, y*settings.TILE_SIZE))

        
            
    
