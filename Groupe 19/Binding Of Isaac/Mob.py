import pygame
from random import randint, randrange

pygame.init()

# Add a timer for adding mobs
ADDMOB = pygame.USEREVENT + 1
pygame.time.set_timer(ADDMOB, 5000)  # Add a mob every 5 seconds

mobs = []
screen = pygame.display.set_mode((1000, 800))

zombie1 = pygame.image.load("assets/Graphics/player-rick.png").convert_alpha()
zombie1 = pygame.transform.scale(zombie1, (100, 100))
zombie2 = pygame.image.load("assets/Graphics/player-princess.png").convert_alpha()
zombie2 = pygame.transform.scale(zombie2, (100, 100))

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

def add_mob(max_mobs=4):
    global mobs

    entry_point = (1000,400)
    min_distance_from_entry = 100  # Minimum distance from entry point
    while len(mobs) < max_mobs:
        mob_image = zombie1 if randrange(0, 2) == 0 else zombie2
        mob_x, mob_y = randint(0, screen.get_width()), randint(0, screen.get_height())

        if ((mob_x - entry_point[0]) ** 2 + (mob_y - entry_point[1]) ** 2) ** 0.5 < min_distance_from_entry:
            continue

        mob = Mob(mob_image, mob_x, mob_y)

        if any(mob.intersects(other_mob) for other_mob in mobs) or mob.rect.right >= 700 or mob.rect.bottom >= 600 or mob.rect.left < 0 or mob.rect.top < 0:
            continue

        mobs.append(mob)
        mob.draw(screen)  # Draw the mob on the screen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Add a mob when the timer event occurs
        if event.type == ADDMOB:
            add_mob()

    # Draw all the mobs
    for mob in mobs:
        mob.draw(screen)

    pygame.display.update()

    pygame.time.Clock().tick(60)