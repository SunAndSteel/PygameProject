from RoomModel import Room
import pygame

class RoomView():
    def __init__(self):
        self.tile_map = Room().generate_room(Room.row, Room.col)

    def draw_from_matrix(self, screen):
        """
        Affiche la salle sur l'écran à partir de la matrice.

        La matrice est une liste de listes, chaque élément de la liste
        représente une ligne de la salle et contient des éléments qui
        représentent les cases de la salle. Les éléments de la liste sont
        des entiers qui peuvent prendre les valeurs suivantes :
            - 0 : case vide
            - 1 : mur
            - 2 : porte (non implémenté)
        """
        img_wall = pygame.image.load('wall_tile.png')

        for y in self.tile_map:
            for x in y:
                if x == 1:
                    screen.blit(img_wall, (16*x, 16*y))
                    pygame.draw.rect(self.img_wall, "black", (0, 0, 32, 32), 1)
        