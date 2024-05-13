import os

import pygame

import Configurations

HAUTEUR, LARGEUR = 800, 800

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        path_image = os.path.join(os.path.dirname(__file__), "ressources_entity_hero", "player-princess.png")
        self.image = pygame.image.load(path_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (HAUTEUR // 2, LARGEUR // 2)
        self.speed = 2.5
        self.strenght_power = 1
        self.health = 100
        self.max_health = 100

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_q]:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += self.speed
        if key[pygame.K_UP] or key[pygame.K_z]:
            self.rect.y -= self.speed
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.y += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > HAUTEUR - self.rect.width:
            self.rect.x = HAUTEUR - self.rect.width
        if self.rect.y > LARGEUR - self .rect.height:
            self.rect.y = LARGEUR - self.rect.height

clock = pygame.time.Clock()
screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
pygame.display.set_caption("test")
running = True
entity = Entity()
all_sprites = pygame.sprite.Group()
all_sprites.add(entity)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(120)