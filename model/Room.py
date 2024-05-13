import pygame
class Room:
    def __init__(self, number):
        self._number = number
        self._tile_size = 32
        self._tile_map = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.tile_colors = {
            0: (0, 0, 0),  # White
            1: (255, 255, 255) # Black
        }

    def draw(self, screen):
        for y, row in enumerate(self._tile_map):
            for x, tile in enumerate(row):
                color = self.tile_colors[tile]
                rect = pygame.Rect(
                    x * self._tile_size, y * self._tile_size, self._tile_size, self._tile_size)
                pygame.draw.rect(screen, color, rect)
    


                    
