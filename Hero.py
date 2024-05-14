import json
import pygame
from Entity import Entity

pygame.init()
HAUTEUR, LARGEUR = 800, 800
screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
clock = pygame.time.Clock()


class Hero(Entity):
    def __init__(self, file_path):
        super().__init__(path=file_path)
        self.load_from_json(file_path)

    def load_from_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                hero_data = json.load(file)
                self.speed = hero_data.get("speed", 2.5)
                self.bonus = hero_data.get("bonus", [])
                self.armes = hero_data.get("armes", [])
                self.shield = hero_data.get("shield", None)
                self.image_path = hero_data.get("image_path")
                if self.image_path:
                    self.load_entity_image(self.image_path)
                self.rect = self.image.get_rect()
                self.rect.center = (HAUTEUR // 2, LARGEUR // 2)
                self.name = hero_data.get("name", "Hero")
        except Exception as e:
            print(f"Error loading hero data from JSON: {e}")


hero = Hero("Entitys/Mobs/Hero/hero.json")
all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
