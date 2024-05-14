import heapq
import random
from RoomType import RoomType

class Map:
    def __init__(self):
        self._rooms = 10
        self._tile_map = self.__generate_map(self._col, self._row)



    def __generate_map(self):
        """Matrice qui représente les salles
        """


# Constants
EMPTY = 0
START = 1
FINAL = 2
PATH = 3

# Function to generate a random map


def generate_map(width, height):
    """
    Fonction pour generer une carte aleatoire
    """
    map_array = [[EMPTY for _ in range(width)] for _ in range(height)]

    # Choose random coordinates for the starting room
    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)
    map_array[start_y][start_x] = START

    # Choose random coordinates for the final room (ensure it's not the same as the starting room)
    final_x, final_y = start_x, start_y
    while (final_x, final_y) == (start_x, start_y):
        final_x = random.randint(0, width - 1)
        final_y = random.randint(0, height - 1)
    map_array[final_y][final_x] = FINAL

    # Connect the starting and final rooms
    connect_rooms(map_array, start_x, start_y, final_x, final_y)

    return map_array

# Function to connect the starting and final rooms


def connect_rooms(map_array, start_x, start_y, final_x, final_y):
    """
    Trouver les chemins entre les deux salles
    """
    frontier = []
    heapq.heappush(frontier, (0, (start_x, start_y)))
    came_from = {}
    cost_so_far = {}
    came_from[(start_x, start_y)] = None
    cost_so_far[(start_x, start_y)] = 0

    while frontier:
        current_cost, current = heapq.heappop(frontier)

        if current == (final_x, final_y):
            break

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = current[0] + dx, current[1] + dy

            if 0 <= next_x < len(map_array[0]) and 0 <= next_y < len(map_array):
                new_cost = current_cost + 1

                if (next_x, next_y) not in cost_so_far or new_cost < cost_so_far[(next_x, next_y)]:
                    cost_so_far[(next_x, next_y)] = new_cost
                    priority = new_cost + \
                        abs(final_x - next_x) + \
                        abs(final_y - next_y)
                    heapq.heappush(frontier, (priority, (next_x, next_y)))
                    came_from[(next_x, next_y)] = current

    # Mark the path from the starting room to the final room
    current = (final_x, final_y)
    while current != (start_x, start_y):
        map_array[current[1]][current[0]] = PATH
        current = came_from[current]

# Function to display the map
def display_map(map_array):
    for row in map_array:
        print(" ".join(str(cell) for cell in row))
# Example usage
width = 10
height = 10
map_array = generate_map(width, height)
display_map(map_array)


