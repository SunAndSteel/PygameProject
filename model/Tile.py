import pygame



class Tile(pygame.sprite.Sprite):
    def __init__(self, material):
        super().__init__()
        self.material = material


        