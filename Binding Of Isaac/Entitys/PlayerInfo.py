import pygame

HAUTEUR, LARGEUR = 800, 800

class PlayerInfo(pygame.sprite.Sprite):
    def __init__(self, entity):
        super().__init__()
        self.__entity = entity
        self.__font = pygame.font.SysFont("Arial", 24)
        self.__show_info = False
        self.__image = None
        self.__rect = None
        self.update_image()

    def update_image(self):
        info_surface = pygame.Surface((200, 100))
        info_surface.fill((0, 0, 0))
        info = [
            f"Nom: {self.entity.name}",
            f"Vitesse: {self.entity.speed}",
            f"Force: {self.entity.strength_power}",
            f"Santé: {self.entity.health}/{self.entity.max_health}"
        ]
        for i, text in enumerate(info):
            text_render = self.font.render(text, True, (255, 255, 255))
            info_surface.blit(text_render, (10, 10 + i * 20))
        self.image = info_surface
        self.rect = self.image.get_rect(topright=(LARGEUR - 10, 10))

    def update(self):
        if self.show_info:
            self.update_image()

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, value):
        self.__entity = value

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        self.__font = value

    @property
    def show_info(self):
        return self.__show_info

    @show_info.setter
    def show_info(self, value):
        self.__show_info = value

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

class PlayerInfoSprite(pygame.sprite.Sprite):
    def __init__(self, player_info):
        super().__init__()
        self.__player_info = player_info

    def update(self):
        self.player_info.update()
        self.image = self.player_info.image
        self.rect = self.player_info.rect

    @property
    def player_info(self):
        return self.__player_info

    @player_info.setter
    def player_info(self, value):
        self.__player_info = value
