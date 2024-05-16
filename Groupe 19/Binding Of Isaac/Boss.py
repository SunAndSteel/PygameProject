import json
import pygame
import random
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
        self.speed = 8

    def update(self):
        self.rect.center += self.direction * self.speed  # Move in the stored direction
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):  # If the fireball is outside the screen
            self.kill()  # Remove the fireball

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class FireWall(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        image = pygame.image.load('assets/Graphics/Projectiles/firewall.png')  # Load the firewall image
        self.image = pygame.transform.scale(image, (100, 150))
        self.rect = self.image.get_rect(center=start_pos)
        self.direction = pygame.Vector2(target_pos) - self.rect.center  # Calculate the direction to the target
        self.direction.normalize_ip()  # Normalize the direction vector
        self.speed = 7

    def update(self):
        self.rect.center += self.direction * self.speed  # Move in the stored direction
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):  # If the firewall is outside the screen
            self.kill()  # Remove the firewall

    def draw(self, surface):
        surface.blit(self.image, self.rect)



class Boss(Entity):
    def __init__(self, image, x, y, hero, path="Entitys/Mobs/Boss/boss.json"):
        super().__init__(path)
        self.fury_mode = False
        self.resistance = 0
        self.level = 150
        self.load_boss_data(path)
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.last_attack_time = pygame.time.get_ticks()
        self.x = x
        self.y = y
        self.target = hero
        self.Id = 4
        self.health = 1000
        self.last_spawn_time = pygame.time.get_ticks()
        self.movement_timer = 0
        self.change_movement_time = 5000
        self.die_song = pygame.mixer.Sound('assets/Sound/nein.mp3')

    def update(self):
        self.spawn_obstacles()
        super().update()

    def load_boss_data(self, path):
        try:
            with open(path, 'r') as file:
                boss_data = json.load(file)
                self.fury_mode = boss_data.get("fury_mode", self.fury_mode)
                self.resistance = boss_data.get("resistance", self.resistance)
                self.level = boss_data.get("level", self.level)
                self.Id = boss_data.get("Id", self.Id)
                self.health = boss_data.get("health", self.health)
        except FileNotFoundError:
            print(f"Erreur : fichier JSON introuvable - {path}")
        except json.JSONDecodeError:
            print(f"Erreur : fichier JSON malformé - {path}")
        except Exception as e:
            print(f"Erreur lors du chargement des données depuis le fichier JSON: {e}")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def attack(self, target, projectiles=None):
        if self.Id == 4:
            from main import projectiles
            current_time = pygame.time.get_ticks()
            if current_time - self.last_attack_time >= (500 if self.fury_mode else 1500):
                attack_type = random.choice(['fireball', 'firewall'])
                self.die_song.play()
                if attack_type == 'fireball':
                    fireball = Fireball(self.rect.center, target.rect.center)
                    projectiles.add(fireball)
                elif attack_type == 'firewall':
                    firewall = FireWall(self.rect.center, target.rect.center)
                    projectiles.add(firewall)
                self.last_attack_time = current_time

    def hurt(self, damage, mobs):
        self.health -= damage
        print(self.health)
        if self.health in range(0, 500):
            self.fury_mode = True

        if self.health <= 0:
            from main import etage, level
            mobs.remove(self)
            self.kill()
            global etage, level
            etage += 1  # Increment the floor when the boss is killed
            level = 1

    def spawn_obstacles(self):
        if self.Id == 4:
            from Mob_spawn import add_obstacle
            from main import hero
            count_time = pygame.time.get_ticks()
            if count_time - self.last_spawn_time >= 10000:
                print('Obstacle spawned by the boss')
                add_obstacle(hero)
                self.last_spawn_time = count_time
