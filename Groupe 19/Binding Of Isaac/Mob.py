import json
import pygame
from Boss import Boss
from math import sqrt
from Hero import *


HAUTEUR, LARGEUR = 800, 800

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
clock = pygame.time.Clock()


class Mob(Boss):
    def __init__(self, image, x,y, target,path = 'Entitys/Mobs/Normal_Mobs/RandomMob.json'):
        super().__init__(path)
        self.health = 100
        self.deplacement = "right-left"
        self.level = 50
        self.load_mob_data(path)
        self.target = target  # Le joueur que le mob doit poursuivre
        self.attack_range = 30  # Define the attack range of the mob
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.last_attack_time = pygame.time.get_ticks()  # Store the time of the last attack

    def load_mob_data(self, path):
        try:
            with open(path, 'r') as file:
                mob_data = json.load(file)
                self.health = mob_data.get("health", self.health)
                self.deplacement = mob_data.get("deplacement", self.deplacement)
                self.level = mob_data.get("level", self.level)
        except FileNotFoundError:
            print(f"Erreur : fichier JSON introuvable - {path}")
        except json.JSONDecodeError:
            print(f"Erreur : fichier JSON malformé - {path}")
        except Exception as e:
            print(f"Erreur lors du chargement des données depuis le fichier JSON: {e}")

    def hurt(self, damage, mobs):
        self.health -= damage
        print(f"Mob health: {self.health}")
        if self.health <= 0:
            self.kill(mobs)  # Remove the mob if its health reaches 0

    def kill(self, mobs):
        if self in mobs:
            mobs.remove(self)
        super().kill()  # Call the kill method of the superclass

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


    def attack(self, target):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000:  # Check if 1 second has passed since the last attack
            dist = sqrt((self.rect.x - self.target.rect.x) ** 2 + (self.rect.y - self.target.rect.y) ** 2)
            if dist <= self.attack_range:
                target.hurt(10)
            self.last_attack_time = current_time  # Update the last attack time


    def intersects(self, other):
        return self.rect.colliderect(other.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

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

