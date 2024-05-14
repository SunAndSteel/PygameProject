import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, name, drop_rate):
        super().__init__(self)
        self.name = name
        self.drop_rate = 5


def used(self):
    pass