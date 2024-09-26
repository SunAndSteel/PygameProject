import pygame


"""
Une MapModel est une matrice qui contient des rooms.
Son implémentation est indépentante de la MapView.


"""
class Map:
    def __init__(self, path):
        self.path = path
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()