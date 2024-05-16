import pygame

HAUTEUR, LARGEUR = 800, 800

class BossInfoShowed(pygame.sprite.Sprite):
    def __init__(self, boss):
        super().__init__()
        self.__boss = boss
        self.__font = pygame.font.SysFont("Arial", 18)
        self.__image = None
        self.__rect = None
        self.update_image()

    def update_image(self):
        info_surface = pygame.Surface((200, 50))
        info_surface.fill((0, 0, 0))
        info = [
            f"Nom: {self.boss.name}",
            f"Niveau: {self.boss.level}"
        ]
        for i, text in enumerate(info):
            text_render = self.font.render(text, True, (255, 255, 255))
            info_surface.blit(text_render, (10, 10 + i * 20))
        self.image = info_surface
        self.rect = self.image.get_rect(midbottom=self.boss.rect.midtop)

    def update(self):
        self.update_image()

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, value):
        self.__boss = value

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        self.__font = value

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
