import json
import pygame
import random
from Entitys.BossInfoShowed import BossInfoShowed
from Entity import Entity


HAUTEUR, LARGEUR = 800, 800
pygame.init()
screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
clock = pygame.time.Clock()

class Fireball(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        image = pygame.image.load('assets/Graphics/Projectiles/fireball.png')  # Load the fireball image
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect(center=start_pos)
        self.direction = pygame.Vector2(target_pos) - self.rect.center  # Calculate the direction to the target
        self.direction.normalize_ip()  # Normalize the direction vector
        self.speed = 5

    def update(self):
        self.rect.center += self.direction * self.speed  # Move in the stored direction
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):  # If the fireball is outside the screen
            self.kill()  # Remove the fireball

class FireWall(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        image = pygame.image.load('assets/Graphics/Projectiles/firewall.png')  # Load the firewall image
        self.image = pygame.transform.scale(image, (100, 150))
        self.rect = self.image.get_rect(center=start_pos)
        self.direction = pygame.Vector2(target_pos) - self.rect.center  # Calculate the direction to the target
        self.direction.normalize_ip()  # Normalize the direction vector
        self.speed = 2

    def update(self):
        self.rect.center += self.direction * self.speed  # Move in the stored direction
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):  # If the firewall is outside the screen
            self.kill()  # Remove the firewall

class Boss(Entity):
    def __init__(self, image, x, y, hero, path = "Entitys/Mobs/Boss/boss.json"):
        super().__init__(path)
        self.fury_mode = False
        self.resistance = 0
        self.mouvements = "right-left"
        self.level = 150
        self.load_boss_data(path)
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.last_attack_time = pygame.time.get_ticks()  # Store the time of the last attack
        print("hello")


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

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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


    def attack(self, target):
        from main import projectiles
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 5000:  # Check if 5 seconds have passed since the last attack
            attack_type = random.choice(['fireball', 'firewall'])
            if attack_type == 'fireball':
                fireball = Fireball(self.rect.center, target.rect.center)
                projectiles.add(fireball)  # Add the fireball to the projectiles group
            elif attack_type == 'firewall':
                firewall = FireWall(self.rect.center, target.rect.center)
                projectiles.add(firewall)  # Add the firewall to the projectiles group
            self.last_attack_time = current_time  # Update the last attack time

    def hurt(self, damage, mobs):
        self.health -= damage
        print(self.health)
        if self.health <= 0:
            mobs.remove(self)  # Remove the boss from the mobs list
            self.kill()  # Remove the boss from all sprite groups