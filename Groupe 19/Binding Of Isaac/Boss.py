import json
import pygame

from Entitys.BossInfoShowed import BossInfoShowed
from Entity import Entity

HAUTEUR, LARGEUR = 800, 800
pygame.init()
screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
clock = pygame.time.Clock()

class Boss(Entity):
    def __init__(self, path):
        super().__init__(path)
        self.fury_mode = False
        self.resistance = 0
        self.mouvements = "right-left"
        self.level = 150
        self.load_boss_data(path)

    def load_boss_data(self, path):
        try:
            with open(path, 'r') as file:
                boss_data = json.load(file)
                self.fury_mode = boss_data.get("fury_mode", self.fury_mode)
                self.resistance = boss_data.get("resistance", self.resistance)
                self.mouvements = boss_data.get("mouvements", self.mouvements)
                self.level = boss_data.get("level", self.level)
        except FileNotFoundError:
            print(f"Erreur : fichier JSON introuvable - {path}")
        except json.JSONDecodeError:
            print(f"Erreur : fichier JSON malformé - {path}")
        except Exception as e:
            print(f"Erreur lors du chargement des données depuis le fichier JSON: {e}")



    def spawn(self):
        print("Le boss apparait")


    def update(self):
        super().update()
        if self.mouvements in ["up-down", "down-up"]:
            self.rect.y += self.speed
            if self.rect.top < 0:
                self.rect.top = 0
                self.speed = -self.speed
            elif self.rect.bottom > HAUTEUR:
                self.rect.bottom = HAUTEUR
                self.speed = -self.speed
        elif self.mouvements in ["left-right", "right-left"]:
            self.rect.x += self.speed
            if self.rect.left < 0:
                self.rect.left = 0
                self.speed = -self.speed
            elif self.rect.right > LARGEUR:
                self.rect.right = LARGEUR
                self.speed = -self.speed

    def show_informations(self):
        super().show_informations()
        if self.show_player_information:
            info_surface = pygame.Surface((200, 50))
            info_surface.fill((0, 0, 0))
            info = [
                f"Nom: {self.name}",
                f"Niveau: {self.level}"
            ]
            font = pygame.font.SysFont("Arial", 20)
            # Parcourt la liste des textes avec leur index Ce n'est pas mon code bien sur mais le fruit de recherches approfondie sur plusieurs topics pygame
            for i, text in enumerate(info):
                # Rend le texte avec une police spécifique et une couleur blanche
                text_render = font.render(text, True, (255, 255, 255))
                # Place le texte rendu verticalement sur la surface
                info_surface.blit(text_render, (10, 10 + i * 20))
            # Affiche la surface d'informations au-dessus du personnage dans le jeu
            screen.blit(info_surface, (self.rect.centerx - info_surface.get_width() // 2, self.rect.top - 30))
