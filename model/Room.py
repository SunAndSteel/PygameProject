import pygame
from Material import Material
from Door import Door

class Room:
    def __init__(self, doors):
        self._items_of_room = [] 
        self._doorsNumbers = Door.DOORS
        self._tile_size = 32
        self._col = 40
        self._row = 20
        self._tile_map = self.__generate_room(self._col, self._row)
        self.tile_skin = Material.Material.WALL

    def draw(self, screen):
        """
        Affiche la salle sur l'écran à partir de la matrice
        """
        for y, row in enumerate(self._tile_map):
            for x, tile in enumerate(row):
                color = self.tile_colors[tile]
                rect = pygame.Rect(x * self._tile_size, y * self._tile_size, self._tile_size, self._tile_size)
                pygame.draw.rect(screen, color, rect)
    
    def __generate_room(self, cols, rows):
        """
        Génération d'une matrice de représentant la bordure de la salle
        """
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    matrix[i][j] = 1
        return matrix


                    
