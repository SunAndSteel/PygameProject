import json
import pygame
import random
from Entity import Entity

HAUTEUR, LARGEUR = 800, 800
pygame.init()
screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
clock = pygame.time.Clock()

class Fireball(pygame.sprite.Sprite):
    '''
    Classe Fireball : Classe représentant les boules de feu lancées par le boss
    '''
    def __init__(self, start_pos, target_pos):
        super().__init__()
        image = pygame.image.load('assets/Graphics/Projectiles/fireball.png')
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect(center=start_pos)
        self.direction = pygame.Vector2(target_pos) - self.rect.center
        self.direction.normalize_ip()
        self.speed = 8

    def update(self):
        self.rect.center += self.direction * self.speed
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class FireWall(pygame.sprite.Sprite):
    '''
    Classe FireWall : Classe représentant le mur de feu lancé par le boss
    '''
    def __init__(self, start_pos, target_pos):
        super().__init__()
        image = pygame.image.load('assets/Graphics/Projectiles/firewall.png')
        self.image = pygame.transform.scale(image, (100, 150))
        self.rect = self.image.get_rect(center=start_pos)
        self.direction = pygame.Vector2(target_pos) - self.rect.center
        self.direction.normalize_ip()
        self.speed = 7

    def update(self):
        self.rect.center += self.direction * self.speed
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)



class Boss(Entity):
    '''
    Classe Boss : Classe représentant le boss du jeu
    '''
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
        '''
        Méthode pour charger les données du boss depuis un fichier JSON
        '''
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
        '''
        Méthode pour faire attaquer le boss
        '''
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
        '''
        Méthode pour infliger des dégâts au boss
        '''
        self.health -= damage
        print(f"Boss health: {self.health}")
        if self.health in range(0, 500):
            self.fury_mode = True

        if self.health <= 0:
            '''
            Si la santé du boss atteint 0, on va le tuer
            On va aussi incrémenter l'étage et remettre le niveau à 1
            '''
            from main import etage, level
            mobs.remove(self)
            self.kill()
            global etage, level
            etage += 1
            level = 1

    def spawn_obstacles(self):
        '''
        Méthode pour faire apparaitre des obstacles pendant le combat de boss
        '''
        if self.Id == 4:
            from Mob_spawn import add_obstacle
            from main import hero
            count_time = pygame.time.get_ticks()
            if count_time - self.last_spawn_time >= 10000:
                add_obstacle(hero)
                self.last_spawn_time = count_time
