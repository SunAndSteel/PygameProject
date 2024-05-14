import json
import pygame
from Entity import Entity

pygame.init()
HAUTEUR, LARGEUR = 1280, 720


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
                self.weapons = hero_data.get("weapons", [])
                self.shield = hero_data.get("shield", None)
                self.image_path = hero_data.get("image_path")
                if self.image_path:
                    self.load_entity_image(self.image_path)
                self.rect = self.image.get_rect()
                self.rect.center = (HAUTEUR // 2, LARGEUR // 2)
                self.name = hero_data.get("name", "Hero")
        except Exception as e:
            print(f"Error loading hero data from JSON: {e}")

        def attack(self):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Attack")


