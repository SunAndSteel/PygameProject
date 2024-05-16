import pygame

Longueur = 150
Hauteur = 500

class Door(pygame.sprite.Sprite):
    def __init__(self, door_direction):
        super().__init__()
        self.__direction = door_direction
        self.__image = pygame.Surface((500, 150))
        self.__image.fill((255, 0, 0))
        self.__rect = self.__image.get_rect()
        self.__set_position(self.__direction)

    def __set_position(self, door_direction):
        if door_direction == "nord":
            self.__rect.center = (Longueur / 2, 0)
        elif door_direction == "sud":
            self.__rect.center = (Longueur / 2, Hauteur)
        elif door_direction == "ouest":
            self.__rect.center = (0, Hauteur / 2)
        elif door_direction == "est":
            self.__rect.center = (Longueur, Hauteur / 2)

    """
    GETTERS AND SETTERS FOR Door's Attributes
    """
    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, value):
        self.__rect = value

    """
    #-----------------------------------#
    """
