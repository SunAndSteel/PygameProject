
import json
import pygame
from Entity import Entity
from math import sqrt
from Weapons import *

pygame.init()
HAUTEUR, LARGEUR = 1280, 720

clock = pygame.time.Clock()
gun = Gun()
knife = Knife()
sword = Sword()

class Hero(Entity):
    def __init__(self, file_path):
        super().__init__(path=file_path)
        self.load_from_json(file_path)
        self.__rage_end_time = 0
        self.__normal_knife_range = 100
        self.__normal_sword_range = 150
        self.__knife_range = self.__normal_knife_range
        self.__sword_range = self.__normal_sword_range
        self.__health = 200
        self.__max_health = 200
        self.__health_bar_length = 400
        self.__health_ratio = self.__max_health / self.__health_bar_length
        self.__last_attack_time = pygame.time.get_ticks()
        self.__weapon = gun
        self.__shield = 0
        self.__max_shield = 100
        self.__shield_bar_length = 400
        self.__shield_ratio = self.__max_shield / self.__shield_bar_length
        self.__shield_state = False
        self.__crosshair_image = pygame.image.load('assets/Graphics/crosshair.png').convert_alpha()
        self.__crosshair_image = pygame.transform.scale(self.__crosshair_image, (30, 30))
        self.__crosshair_pos = [0, 0]
        self.__heart_image = pygame.transform.scale(pygame.image.load("assets/Graphics/HUD/HUD_heart.png"), (40, 40))
        self.__shield_image = pygame.transform.scale(pygame.image.load("assets/Graphics/HUD/HUD_shield.png"), (50, 50))
        self.__in_boss_room = False
        self.__mouvements = "perso"

    def load_from_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                hero_data = json.load(file)
                self.speed = hero_data.get("speed", 2.5)
                self.bonus = hero_data.get("bonus", [])
                self.shield = hero_data.get("shield", None)
                self.image_path = hero_data.get("image_path")
                if self.image_path:
                    self.load_entity_image(self.image_path)
                self.rect = self.image.get_rect()
                self.rect.center = (HAUTEUR // 2, LARGEUR // 2)
                self.name = hero_data.get("name", "Hero")
        except Exception as e:
            print(f"Error loading hero data from JSON: {e}")

    @property
    def rage_end_time(self):
        return self.__rage_end_time

    @rage_end_time.setter
    def rage_end_time(self, value):
        self.__rage_end_time = value

    @property
    def normal_knife_range(self):
        return self.__normal_knife_range

    @normal_knife_range.setter
    def normal_knife_range(self, value):
        self.__normal_knife_range = value

    @property
    def normal_sword_range(self):
        return self.__normal_sword_range

    @normal_sword_range.setter
    def normal_sword_range(self, value):
        self.__normal_sword_range = value

    @property
    def knife_range(self):
        return self.__knife_range

    @knife_range.setter
    def knife_range(self, value):
        self.__knife_range = value

    @property
    def sword_range(self):
        return self.__sword_range

    @sword_range.setter
    def sword_range(self, value):
        self.__sword_range = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def max_health(self):
        return self.__max_health

    @max_health.setter
    def max_health(self, value):
        self.__max_health = value

    @property
    def health_bar_length(self):
        return self.__health_bar_length

    @health_bar_length.setter
    def health_bar_length(self, value):
        self.__health_bar_length = value

    @property
    def health_ratio(self):
        return self.__health_ratio

    @health_ratio.setter
    def health_ratio(self, value):
        self.__health_ratio = value

    @property
    def last_attack_time(self):
        return self.__last_attack_time

    @last_attack_time.setter
    def last_attack_time(self, value):
        self.__last_attack_time = value

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, value):
        self.__weapon = value

    @property
    def shield(self):
        return self.__shield

    @shield.setter
    def shield(self, value):
        self.__shield = value

    @property
    def max_shield(self):
        return self.__max_shield

    @max_shield.setter
    def max_shield(self, value):
        self.__max_shield = value

    @property
    def shield_bar_length(self):
        return self.__shield_bar_length

    @shield_bar_length.setter
    def shield_bar_length(self, value):
        self.__shield_bar_length = value

    @property
    def shield_ratio(self):
        return self.__shield_ratio

    @shield_ratio.setter
    def shield_ratio(self, value):
        self.__shield_ratio = value

    @property
    def shield_state(self):
        return self.__shield_state

    @shield_state.setter
    def shield_state(self, value):
        self.__shield_state = value

    @property
    def crosshair_image(self):
        return self.__crosshair_image

    @crosshair_image.setter
    def crosshair_image(self, value):
        self.__crosshair_image = value

    @property
    def crosshair_pos(self):
        return self.__crosshair_pos

    @crosshair_pos.setter
    def crosshair_pos(self, value):
        self.__crosshair_pos = value

    @property
    def heart_image(self):
        return self.__heart_image

    @heart_image.setter
    def heart_image(self, value):
        self.__heart_image = value

    @property
    def shield_image(self):
        return self.__shield_image

    @shield_image.setter
    def shield_image(self, value):
        self.__shield_image = value

    @property
    def in_boss_room(self):
        return self.__in_boss_room

    @in_boss_room.setter
    def in_boss_room(self, value):
        self.__in_boss_room = value

    @property
    def mouvements(self):
        return self.__mouvements

    @mouvements.setter
    def mouvements(self, value):
        self.__mouvements = value

    def attack(self, mobs):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_attack_time >= 1000:
                if isinstance(self.weapon, Knife):
                    for mob in mobs:
                        dist = sqrt((self.rect.x - mob.rect.x) ** 2 + (self.rect.y - mob.rect.y) ** 2)
                        if dist <= self.knife_range:
                            mob.hurt(20, mobs)
                elif isinstance(self.weapon, Sword):
                    for mob in mobs:
                        dist = sqrt((self.rect.x - mob.rect.x) ** 2 + (self.rect.y - mob.rect.y) ** 2)
                        if dist <= self.sword_range:
                            mob.hurt(self.weapon.damage, mobs)
                elif isinstance(self.weapon, Gun):
                    self.weapon.fire(self, mobs)
                self.last_attack_time = current_time

    def hurt(self, damage):
        if self.shield_state and self.shield > 0:
            self.shield -= damage
        else:
            self.shield_state = False
            self.health -= damage
            print("ouile")
            print(f"Hero health: {self.health}")
            if self.__health <= 0:
                pygame.quit()

    def basic_health(self):
        from main import screen
        pygame.draw.rect(screen, (255, 0, 0), (45, 10, self.health / self.health_ratio, 25))
        pygame.draw.rect(screen, (0, 0, 0), (45, 10, self.health_bar_length, 25), 2)

    def basic_shield(self):
        from main import screen
        pygame.draw.rect(screen, (0, 0, 255), (45, 60, self.shield / self.shield_ratio, 25))
        pygame.draw.rect(screen, (0, 0, 0), (45, 60, self.shield_bar_length, 25), 2)

    def update(self, mobs, obstacles):
        self.basic_health()
        if self.__shield > 0:
            self.basic_shield()
        self.check_obstacle_collision(obstacles)
        self.check_rage_end()
