import pygame
from Item import Item

class Malus(Item):
    def __init__(self, permanent):
        super().__init__()
        self.permanent = False