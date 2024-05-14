import json
import pygame
from Boss import Boss
from Hero import Hero

HAUTEUR, LARGEUR = 800, 800

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
clock = pygame.time.Clock()


class Mob(Boss):
    def __init__(self, path, target):
        super().__init__(path)
        self.resistance = 1
        self.deplacement = "right-left"
        self.level = 50
        self.load_mob_data(path)
        self.target = target  # Le joueur que le mob doit poursuivre

    def load_mob_data(self, path):
        try:
            with open(path, 'r') as file:
                mob_data = json.load(file)
                self.resistance = mob_data.get("resistance", self.resistance)
                self.deplacement = mob_data.get("deplacement", self.deplacement)
                self.level = mob_data.get("level", self.level)
        except FileNotFoundError:
            print(f"Erreur : fichier JSON introuvable - {path}")
        except json.JSONDecodeError:
            print(f"Erreur : fichier JSON malformé - {path}")
        except Exception as e:
            print(f"Erreur lors du chargement des données depuis le fichier JSON: {e}")

    def update(self):
        if self.target:
            if self.rect.x < self.target.rect.x:
                self.rect.x += self.speed
            elif self.rect.x > self.target.rect.x:
                self.rect.x -= self.speed

            if self.rect.y < self.target.rect.y:
                self.rect.y += self.speed
            elif self.rect.y > self.target.rect.y:
                self.rect.y -= self.speed

        super().update()

    def show_informations(self):
        super().show_informations()
        if self.show_player_information:
            info_surface = pygame.Surface((200, 50))
            info_surface.fill((0, 0, 0))
            info = [
                f"Résistance: {self.resistance}",
                f"Deplacement: {self.deplacement}",
                f"Level: {self.level}"
            ]
            for i, text in enumerate(info):
                info_surface.blit(pygame.font.SysFont(None, 20).render(text, True, (255, 255, 255)), (10, i * 20))
            screen.blit(info_surface, (self.rect.x, self.rect.y - 50))
            pygame.display.flip()

if __name__ == '__main__':
    # Assurez-vous d'importer la classe Hero correctement
    hero = Hero("Entitys/Mobs/Hero/hero.json")
    mob = Mob("Entitys/Mobs/Normal_Mobs/RandomMob.json", hero)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(hero)
    all_sprites.add(mob)

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
