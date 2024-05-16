import pygame

pygame.init()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, x, y, effect):
        super().__init__()
        self.__image = pygame.image.load(image).convert_alpha()
        self.__rect = self.__image.get_rect(topleft=(x, y))
        self.__effect = effect

    def intersects(self, other):
        return self.rect.colliderect(other.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def apply_effect(self, hero):
        if self.effect == 'heal':
            if hero.health < hero.max_health:
                hero.health += 10
                print(f"Hero health: {hero.health}")
        elif self.effect == 'speed':
            hero.speed += 3
            print(f"Hero speed: {hero.speed}")
        elif self.effect == 'shield':
            hero.shield_state = True
            if hero.shield < hero.max_shield:
                hero.shield += 20
                print(f"Hero shield: {hero.shield}")
        elif self.effect == 'rage':
            hero.knife_range += 100
            hero.sword_range += 100
            hero.rage_end_time = pygame.time.get_ticks() + 10000
            print(f"Hero attack range: {hero.knife_range} {hero.sword_range}")
        elif self.effect == 'unheal':
            print("ouileaaaaaa")
            hero.hurt(10)
            print(f"Hero health: {hero.health}")

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

    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, value):
        self.__effect = value

