import pygame
from random import randint, randrange, choice

pygame.init()

# Add a timer for adding mobs
ADDMOB = pygame.USEREVENT + 1
pygame.time.set_timer(ADDMOB, 500)  # Add a mob every 5 seconds

mobs = []
screen = pygame.display.set_mode((1280, 720))

mini_hitler = pygame.image.load("assets/Graphics/Mobs/minihitler.png").convert_alpha()
mini_hitler = pygame.transform.scale(mini_hitler, (100, 100))
Soldier = pygame.image.load("assets/Graphics/Mobs/solider.png").convert_alpha()
Soldier = pygame.transform.scale(Soldier, (100, 100))
Gazeur = pygame.image.load("assets/Graphics/Mobs/gazeur.png").convert_alpha()
Gazeur = pygame.transform.scale(Gazeur, (100, 100))


class Mob(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def intersects(self, other):
        return self.rect.colliderect(other.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Boss(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def intersects(self, other):
        return self.rect.colliderect(other.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def intersects(self, other):
        return self.rect.colliderect(other.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def add_mob(max_mobs=5):
    global mobs

    entry_point = (1280,400)
    min_distance_from_entry = 500  # Minimum distance from entry point
    while len(mobs) < max_mobs:
        mob_image = choice([mini_hitler, Soldier, Gazeur])
        mob_x, mob_y = randint(0, screen.get_width()), randint(0, screen.get_height())

        if ((mob_x - entry_point[0]) ** 2 + (mob_y - entry_point[1]) ** 2) ** 0.5 < min_distance_from_entry:
            continue

        mob = Mob(mob_image, mob_x, mob_y)

        if any(mob.intersects(other_mob) for other_mob in mobs) or mob.rect.right >= 1280 or mob.rect.bottom >= 720 or mob.rect.left < 0 or mob.rect.top < 0:
            continue

        mobs.append(mob)
        mob.draw(screen)  # Draw the mob on the screen




