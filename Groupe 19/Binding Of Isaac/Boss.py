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
        self.__image = pygame.transform.scale(image, (50, 50))
        self.__rect = self.__image.get_rect(center=start_pos)
        self.__direction = pygame.Vector2(target_pos) - self.__rect.center  # Calculate the direction to the target
        self.__direction.normalize_ip()  # Normalize the direction vector
        self.__speed = 8

    """
    GETTERS AND SETTERS FOR Fireball()'s attributes
    """
    

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, value):
        self.__image = value
        
    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, value):
        self.__rect = value

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = value

    """
#-------------------------------------#
    """

    def update(self):
        self.rect.center += self.direction * self.speed  # Move in the stored direction
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):  # If the fireball is outside the screen
            self.kill()  # Remove the fireball

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class FireWall(pygame.sprite.Sprite):
    """_summary_

    Args:
        
    """
    def __init__(self, start_pos, target_pos):
        super().__init__()
        image = pygame.image.load('assets/Graphics/Projectiles/firewall.png')  # Load the firewall image
        self.__image = pygame.transform.scale(image, (100, 150))
        self.__rect = self.image.get_rect(center=start_pos)
        self.__direction = pygame.Vector2(target_pos) - self.rect.center  # Calculate the direction to the target
        self.__direction.normalize_ip()  # Normalize the direction vector
        self.__speed = 7


    """
    GETTERS AND SETTERS FOR FireWall()'s attributes
    """

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, value):
        self.__image = value
        
    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, value):
        self.__rect = value

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = value

    """
#-------------------------------------#
    """

    def update(self):
        self.rect.center += self.direction * self.speed  # Move in the stored direction
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):  # If the firewall is outside the screen
            self.kill()  # Remove the firewall

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Boss(Entity):
    def __init__(self, image, x, y, hero, path = "Entitys/Mobs/Boss/boss.json"):
        super().__init__(path)
        self.__fury_mode = False
        self.__resistance = 0
        self.__level = 150
        self.__Id = 4
        self.__health = 1000
        self.__last_spawn_time = pygame.time.get_ticks()
        self.__movement_timer = 0
        self.__change_movement_time = 5000
        self.__load_boss_data(path)
        self.__image = image
        self.__rect = self.image.get_rect(topleft=(x, y))
        self.__last_attack_time = pygame.time.get_ticks()  # Store the time of the last attack
        self.__x = x
        self.__y = y
        self.__target = hero

    """
    GETTER AND SETTERS FOR Boss()'s attributes
    """

    @property
    def fury_mode(self):
        return self.__fury_mode
    
    @fury_mode.setter
    def fury_mode(self, value):
        self.__fury_mode = value

    @property
    def resistance(self):
        return self.__resistance
    
    @resistance.setter
    def resistance(self, value):
        self.__resistance = value

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def Id(self):
        return self.__Id
    
    @Id.setter
    def Id(self, value):
        self.__Id = value

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def last_spawn_time(self):
        return self.__last_spawn_time
    
    @last_spawn_time.setter
    def last_spawn_time(self, value):
        self.__last_spawn_time = value

    @property
    def movement_timer(self):
        return self.__movement_timer
    
    @movement_timer.setter
    def movement_timer(self, value):
        self.__movement_timer = value

    @property
    def change_movement_time(self):
        return self.__change_movement_time
    
    @change_movement_time.setter
    def change_movement_time(self, value):
        self.__change_movement_time = value

    @property
    def last_attack_time(self):
        return self.__last_attack_time
    
    @last_attack_time.setter
    def last_attack_time(self, value):
        self.__last_attack_time = value

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, value):
        self.__rect = value

    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def target(self):
        return self.__target
    
    @target.setter
    def target(self, value):
        self.__target = value


    """
#-------------------------------------#
    """


    def __load_boss_data(self, path):
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

    def update(self):
        super().update()
        if self.movement_timer < self.change_movement_time:
            self.movement_timer += pygame.time.get_ticks()
        else:
            self.change_movement()
            self.movement_timer = 0

        if self.mouvements in ["up-down", "down-up"]:
            self.move_up_down()
        elif self.mouvements in ["left-right", "right-left"]:
            self.move_left_right()
        elif self.mouvements == "carré":
            self.move_square()
        elif self.mouvements == "losange":
            self.move_losange()
        elif self.mouvements == "diagonale":
            self.move_diagonal()

    def move_up_down(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = -self.speed
        elif self.rect.bottom > HAUTEUR:
            self.rect.bottom = HAUTEUR
            self.speed = -self.speed

    def move_left_right(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed = -self.speed
        elif self.rect.right > LARGEUR:
            self.rect.right = LARGEUR
            self.speed = -self.speed

    def move_square(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        if self.rect.left < 0 or self.rect.right > LARGEUR or self.rect.top < 0 or self.rect.bottom > HAUTEUR:
            self.speed = -self.speed

    def move_losange(self):
        if self.rect.left <= 0 or self.rect.right >= LARGEUR or self.rect.top <= 0 or self.rect.bottom >= HAUTEUR:
            self.speed = -self.speed
        if self.speed > 0:
            if self.rect.left > LARGEUR // 2:
                self.rect.x -= self.speed
                self.rect.y += self.speed
            else:
                self.rect.x += self.speed
                self.rect.y -= self.speed
        else:
            if self.rect.left > LARGEUR // 2:
                self.rect.x += self.speed
                self.rect.y -= self.speed
            else:
                self.rect.x -= self.speed
                self.rect.y += self.speed

    def move_diagonal(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed = -self.speed
        elif self.rect.right > LARGEUR:
            self.rect.right = LARGEUR
            self.speed = -self.speed
        elif self.rect.top < 0:
            self.rect.top = 0
            self.speed = -self.speed
        elif self.rect.bottom > HAUTEUR:
            self.rect.bottom = HAUTEUR
            self.speed = -self.speed

    def attack(self, target, projectiles=None):
        if self.Id == 4:

            from main import projectiles
            current_time = pygame.time.get_ticks()
            if current_time - self.last_attack_time >= (500 if self.fury_mode else 1500):
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
        if self.health in range(0, 500):
            self.fury_mode = True

        if self.health <= 0:
            mobs.remove(self)  # Remove the boss from the mobs list
            self.kill()  # Remove the boss from all sprite groups

    def spawn_obstacles(self):
        if self.Id == 4:
            from Mob_spawn import add_obstacle
            from main import hero
            count_time = pygame.time.get_ticks()
            if count_time - self.last_spawn_time >= 10000:
                print('Obstacle spawned by the boss')
                add_obstacle(hero)
                self.last_spawn_time = count_time
