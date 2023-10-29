import random
import pygame as py
import config.settings as settings


# Constants
FLOOR = 0
WALL = 1
DOOR = 2

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
            # Then move vertically
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.dungeon_map[x2][y] = FLOOR
        else:
            # Move vertically
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.dungeon_map[x1][y] = FLOOR
            # Then move horizontally
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.dungeon_map[x][y2] = FLOOR


    def generate_dungeon(self):
        # Generate multiple rooms and connect them
        for i in range(10):  # Example: 10 rooms
            room = Room(random.randint(0, MAP_WIDTH - 10), random.randint(0, MAP_HEIGHT - 10), random.randint(5, 10), random.randint(5, 10))
            self.add_room(room)
        print(f"Total rooms generated: {len(self.rooms)}")
        # Connect the rooms
        for i in range(len(self.rooms) - 1):
            self.connect_rooms(self.rooms[i], self.rooms[i + 1])

    def display_map(self, screen):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                if self.dungeon_map[x][y] == FLOOR:
                    tile = settings.FLOOR_TILE
                else:
                    tile = settings.WALL_TILE
                screen.blit(tile, (x*settings.TILE_SIZE, y*settings.TILE_SIZE))

        
            
    
