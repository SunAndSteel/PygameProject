import os
import pygame
import json

from Entitys.PlayerInfo import PlayerInfo, PlayerInfoSprite

HAUTEUR, LARGEUR = 800, 800
pygame.init()

class Entity(pygame.sprite.Sprite):
    def __init__(self,path):
        super().__init__()
        self.speed = 2.5
        self.strength_power = 1
        self.health = 100
        self.max_health = 100
        self.image = None
        self.rect = None
        self.name = "Entity"
        self.path = path
        self.load_from_json(path)
        self.show_player_information = False

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
        if self.rect.y > LARGEUR - self.rect.height:
            self.rect.y = LARGEUR - self.rect.height

    def show_informations(self):
        self.show_player_information = not self.show_player_information

    def load_from_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                player_data_from_json = json.load(file)
                self.speed = player_data_from_json.get("speed", self.speed)
                self.strength_power = player_data_from_json.get("strength_power", self.strength_power)
                self.health = player_data_from_json.get("health", self.health)
                self.max_health = player_data_from_json.get("max_health", self.max_health)
                image_path = player_data_from_json.get("image_path")
                if image_path is not None or image_path != "":
                    self.load_entiy_image(image_path)
                self.rect = self.image.get_rect()
                self.rect.center = (HAUTEUR // 2, LARGEUR // 2)
                self.name = player_data_from_json.get("name", "Entity")
        except Exception as e:
            print("Erreur lors du chargement des données depuis le fichier JSON:", e)

    def load_entiy_image(self, image_path):
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (75, 75))
        except pygame.error as e:
            print(f"Erreur lors du chargement des données : {image_path}: {e}")


clock = pygame.time.Clock()
screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
pygame.display.set_caption("test")
running = True
entity = Entity("Entitys/Mobs/Boss/Terratae.json")
player_info = PlayerInfo(entity)
all_sprites = pygame.sprite.Group()
all_sprites.add(entity)
player_info_sprite = PlayerInfoSprite(player_info)
all_sprites.add(player_info_sprite)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                entity.show_informations()

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(120)
