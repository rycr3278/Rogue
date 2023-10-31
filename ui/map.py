import random
import pygame as py
import config.settings as settings


# Define map tile constants
FLOOR = 0
WALL = 1
DOOR = 2
TOP_EDGE = 3
RIGHT_EDGE = 4
LEFT_EDGE = 5
RIGHT_TOP_CORNER = 6
LEFT_TOP_CORNER = 7
LEFT_BOTTOM_CORNER = 8
RIGHT_BOTTOM_CORNER = 9
BOTTOM_EDGE = 10
USED_DOOR = 11

# Map dimensions
MAP_WIDTH = 48
MAP_HEIGHT = 27

# Map safety border to prevent rooms from being generated on edges
SAFETY_MARGIN = 2

class Room:
    def __init__(self, x, y, width, height):
        # Initialize the room based on its top-left corner, width, and height
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def create_room(self, dungeon_map):
        # Fill the defined area of the dungeon map with floor tiles
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.height):
                dungeon_map[x][y] = FLOOR

class DungeonMap:    
    def __init__(self):
        # Initialize the dungeon map filled with wall tiles and generate the dungeon layout
        self.dungeon_map = [[WALL for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
        self.rooms = []
        self.door_coordinates = {"top":(0,0), "bottom":(0,0), "left":(0,0), "right":(0,0)}
        self.generate_dungeon()
        
        # Initialize display_tiles with the same dimensions as dungeon_map
        self.display_tiles = [[None for _ in range(MAP_HEIGHT)] for _ in range(MAP_WIDTH)]
        self.generate_tiles()
        
        print('new dungeon generated')
        
    def generate_tiles(self):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                if self.dungeon_map[x][y] == LEFT_TOP_CORNER:
                    tile = settings.LEFT_TOP_CORNER_TILE
                elif self.dungeon_map[x][y] == RIGHT_TOP_CORNER:
                    tile = settings.RIGHT_TOP_CORNER_TILE
                elif self.dungeon_map[x][y] == LEFT_BOTTOM_CORNER:
                    tile = settings.LEFT_BOTTOM_CORNER_TILE
                elif self.dungeon_map[x][y] == RIGHT_BOTTOM_CORNER:
                    tile = settings.RIGHT_BOTTOM_CORNER_TILE
                elif self.dungeon_map[x][y] == TOP_EDGE:
                    tile = settings.TOP_EDGE_TILE
                elif self.dungeon_map[x][y] == RIGHT_EDGE:
                    tile = settings.RIGHT_EDGE_TILE
                elif self.dungeon_map[x][y] == LEFT_EDGE:
                    tile = settings.LEFT_EDGE_TILE
                elif self.dungeon_map[x][y] == FLOOR:
                    tile = settings.FLOOR_TILE
                elif self.dungeon_map[x][y] == USED_DOOR:
                    tile = settings.USED_DOOR_TILE  
                elif self.dungeon_map[x][y] == DOOR:
                    tile = settings.DOOR_TILE
                elif self.dungeon_map[x][y] == BOTTOM_EDGE:
                    tile = settings.FLOOR_TILE
                else:
                    tile = settings.get_random_wall_tile()
                
                self.display_tiles[x][y] = tile

    def add_room(self, room):
        # Check if room overlaps with existing rooms or is too close to the edges.
        overlap = False
        for r in self.rooms:
            if (room.x < r.x + r.width and room.x + room.width > r.x and
                room.y < r.y + r.height and room.y + room.height > r.y):
                overlap = True
                break
        
        # Check if room is too close to the edges
        too_close_to_edge = (room.x < SAFETY_MARGIN or 
                             room.y < SAFETY_MARGIN or 
                             room.x + room.width > MAP_WIDTH - SAFETY_MARGIN or 
                             room.y + room.height > MAP_HEIGHT - SAFETY_MARGIN)
        
        if not overlap and not too_close_to_edge:
            room.create_room(self.dungeon_map)
            self.rooms.append(room)
        else:
            print("Room is either overlapping with another room or too close to the edge.")

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
                    self.dungeon_map[x][y1 + 3] = FLOOR  # Add tile below for 3-tile-wide corridor
            # Then move vertically
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.dungeon_map[x2][y] = FLOOR
                if x2 + 1 < MAP_WIDTH:  # Ensure we're not out of bounds
                    self.dungeon_map[x2 + 1][y] = FLOOR  # Add tile to the right for 2-tile-wide corridor
                    self.dungeon_map[x2 + 2][y] = FLOOR  # Add tile to the right for 3-tile-wide corridor
                    self.dungeon_map[x2 + 3][y] = FLOOR  # Add tile to the right for 3-tile-wide corridor
        else:
            # Move vertically
            for y in range(min(y1, y2), max(y1, y2) + 1):
                self.dungeon_map[x1][y] = FLOOR
                if x1 + 1 < MAP_WIDTH:  # Ensure we're not out of bounds
                    self.dungeon_map[x1 + 1][y] = FLOOR  # Add tile to the right for 2-tile-wide corridor
                    self.dungeon_map[x1 + 2][y] = FLOOR  # Add tile to the right for 3-tile-wide corridor
                    self.dungeon_map[x1 + 3][y] = FLOOR  # Add tile to the right for 3-tile-wide corridor
            # Then move horizontally
            for x in range(min(x1, x2), max(x1, x2) + 1):
                self.dungeon_map[x][y2] = FLOOR
                if y2 + 1 < MAP_HEIGHT:  # Ensure we're not out of bounds
                    self.dungeon_map[x][y2 + 1] = FLOOR  # Add tile below for 2-tile-wide corridor
                    self.dungeon_map[x][y2 + 2] = FLOOR  # Add tile below for 3-tile-wide corridor
                    self.dungeon_map[x][y2 + 3] = FLOOR  # Add tile below for 3-tile-wide corridor

    def add_transitional_tiles(self):
        # Add transitional tiles like edges between floor and wall
        for y in range(1, MAP_HEIGHT - 1):
            for x in range(1, MAP_WIDTH - 1):
                if self.dungeon_map[x][y] == FLOOR:
                    top = self.dungeon_map[x][y-1]
                    right = self.dungeon_map[x+1][y]
                    left = self.dungeon_map[x-1][y]
                    bottom = self.dungeon_map[x][y+1]

                    # Check for top edge
                    if top == WALL:
                        self.dungeon_map[x][y] = TOP_EDGE
                    # Check for right edge
                    elif right == WALL:
                        self.dungeon_map[x][y] = RIGHT_EDGE
                    # Check for left edge
                    elif left == WALL:
                        self.dungeon_map[x][y] = LEFT_EDGE
                    elif bottom == WALL:
                        self.dungeon_map[x][y] = BOTTOM_EDGE
            

                        
    def add_corner_tiles(self):
        # Identify and add corner tiles in the dungeon
        for y in range(1, MAP_HEIGHT - 1):  # Start at 1 and end before the last to avoid out of bounds error
            for x in range(1, MAP_WIDTH - 1):
                # Check for left-top corner
                if (self.dungeon_map[x][y] == TOP_EDGE and
                    self.dungeon_map[x][y-1] == WALL and 
                    self.dungeon_map[x-1][y] == WALL):
                    self.dungeon_map[x][y] = LEFT_TOP_CORNER
                    
                # Check for right-top corner
                elif (self.dungeon_map[x][y] == TOP_EDGE and
                    self.dungeon_map[x][y-1] == WALL and 
                    self.dungeon_map[x+1][y] == WALL):
                    self.dungeon_map[x][y] = RIGHT_TOP_CORNER
                    
                # Check for left-bottom corner
                elif (self.dungeon_map[x][y] == FLOOR and
                    self.dungeon_map[x][y-1] == RIGHT_EDGE and 
                    self.dungeon_map[x+1][y] == TOP_EDGE):
                    self.dungeon_map[x][y] = LEFT_BOTTOM_CORNER
                    
                # check for right-bottom corner
                elif (self.dungeon_map[x][y] == FLOOR and
                    self.dungeon_map[x][y-1] == LEFT_EDGE and 
                    self.dungeon_map[x-1][y] == TOP_EDGE):
                    self.dungeon_map[x][y] = RIGHT_BOTTOM_CORNER
                        
                    
    def add_doors(self):
        # Add doors at specific positions in the dungeon
        top_door_exists = False
        right_door_exists = False
        left_door_exists = False
        bottom_door_exists = False
        
        for y in range(1, MAP_HEIGHT - 1):  # only populate top 50% of map with door
            for x in range(MAP_WIDTH // 3, MAP_WIDTH - 1):
                # top door
                if self.dungeon_map[x][y] == TOP_EDGE and not top_door_exists:
                    self.dungeon_map[x][y] = DOOR
                    top_door_exists = True
                    self.door_coordinates["top"] = (x, y)
                    print(f"Added top door at x: {x}, y: {y}")
                    
        for y in range(MAP_HEIGHT // 2, MAP_HEIGHT - 1):  # only populate bottom 50% of map with door
            for x in range(1, MAP_WIDTH - 1):        
                # bottom door
                if self.dungeon_map[x][y] == BOTTOM_EDGE and not bottom_door_exists:
                    self.dungeon_map[x][y+1] = DOOR
                    self.dungeon_map[x+1][y+1] = FLOOR
                    self.dungeon_map[x-1][y+1] = FLOOR
                    bottom_door_exists = True
                    self.door_coordinates["bottom"] = (x, y + 1)
                    print(f"Added bottom door at x: {x}, y: {y}")
                    
        for y in range(MAP_HEIGHT // 2, MAP_HEIGHT - 1):  # only populate left side
            for x in range(1, MAP_WIDTH // 2):           
                # left door
                if self.dungeon_map[x][y] == LEFT_EDGE and not left_door_exists:
                    self.dungeon_map[x-1][y] = DOOR
                    self.dungeon_map[x][y] = FLOOR
                    self.dungeon_map[x-1][y+1] = FLOOR
                    self.dungeon_map[x][y+1] = FLOOR
                    left_door_exists = True
                    self.door_coordinates["left"] = (x - 1, y)
                    print(f"Added left door at x: {x}, y: {y}")
                    
        for y in range(1, MAP_HEIGHT - 1):  # only populate right side
            for x in range(MAP_WIDTH // 2, MAP_WIDTH - 1):           
                # RIGHT  door
                if self.dungeon_map[x][y] == RIGHT_EDGE and not right_door_exists:
                    self.dungeon_map[x+1][y] = DOOR
                    self.dungeon_map[x][y] = FLOOR
                    self.dungeon_map[x+1][y+1] = FLOOR
                    self.dungeon_map[x][y+1] = FLOOR
                    right_door_exists = True
                    self.door_coordinates["right"] = (x + 1, y)
                    print(f"Added right door at x: {x}, y: {y}")
        

        
                    

    def get_door_coordinates(self):
        return self.door_coordinates
        

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
        self.add_corner_tiles()
        self.add_doors()
        


    
                 
    def display_map(self, screen):
        # Render the dungeon map onto the screen 
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                screen.blit(self.display_tiles[x][y], (x * settings.TILE_SIZE, y * settings.TILE_SIZE))