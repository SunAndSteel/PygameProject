import json
import pygame
from Entity import Entity
from math import sqrt
from Weapons import *

pygame.init()
HAUTEUR, LARGEUR = 1280, 720


clock = pygame.time.Clock()


class Hero(Entity):
    def __init__(self, file_path):
        super().__init__(path=file_path)
        self.load_from_json(file_path)
        self.rage_end_time = 0
        self.normal_knife_range = 100  # Define the range of the knife
        self.normal_sword_range = 150  # Define the range of the sword
        self.knife_range = self.normal_knife_range  # Set the initial range of the knife
        self.sword_range = self.normal_sword_range
        self.health = 100  # Define the health of the hero
        self.last_attack_time = pygame.time.get_ticks()  # Store the time of the last attack
        self.weapon = Gun()  # Define the weapon of the hero
        self.shield = 0  # Define the shield of the hero
        self.max_shield = 100
        self.shield_state = False  # Define the state of the shield
        # Load the crosshair image
        self.crosshair_image = pygame.image.load('assets/Graphics/crosshair.png').convert_alpha()
        self.crosshair_image = pygame.transform.scale(self.crosshair_image, (30, 30))  # Scale the image
        self.crosshair_pos = [0, 0]  # Initialize the position of the crosshair



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

    def attack(self, mobs):
        from Mob import Mob
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:  # If left mouse button is clicked
            current_time = pygame.time.get_ticks()
            if current_time - self.last_attack_time >= 1000:  # Check if 1 second has passed since the last attack
                if isinstance(self.weapon, Knife):
                    for mob in mobs:
                        dist = sqrt((self.rect.x - mob.rect.x) ** 2 + (self.rect.y - mob.rect.y) ** 2)
                        if dist <= self.knife_range:
                            mob.hurt(20, mobs)  # Call the hurt method of the Mob class
                elif isinstance(self.weapon, Gun):
                    self.weapon.fire(self, mobs)
                self.last_attack_time = current_time  # Update the last attack time

    def hurt(self, damage):
        if self.shield_state:
            self.shield -= damage
        else:
            self.shield_state = False
            self.health -= damage
            print("ouile")
            print(f"Hero health: {self.health}")
            if self.health <= 0:
                print("Le joueur est mort")

    def update(self, mobs, obstacles):
        super().update()
        self.check_obstacle_collision(obstacles)
        self.check_rage_end()
        self.rotate_to_mouse()  # Add this line to rotate the player to face the mouse

    def rotate_to_mouse(self):
        # Get the position of the mouse
        mouse_pos = pygame.mouse.get_pos()

        # Calculate the angle between the player's position and the mouse position
        rel_x, rel_y = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery
        angle = (180 / math.pi) * math.atan2(rel_y, rel_x)

        # Calculate the position of the crosshair
        crosshair_distance = 60  # Distance from the hero to the crosshair
        self.crosshair_pos[0] = self.rect.centerx + crosshair_distance * math.cos(math.radians(angle))
        self.crosshair_pos[1] = self.rect.centery + crosshair_distance * math.sin(math.radians(angle))


    def check_obstacle_collision(self, obstacles):
            for obstacle in obstacles:
                if self.rect.colliderect(obstacle.rect):
                    obstacle.apply_effect(self)
                    obstacles.remove(obstacle)

    def check_rage_end(self):
        if pygame.time.get_ticks() > self.rage_end_time:
            self.knife_range = self.normal_knife_range
            self.sword_range = self.normal_sword_range

    def draw(self, screen):
        if isinstance(self.weapon, Gun):
            screen.blit(self.crosshair_image, (self.crosshair_pos[0], self.crosshair_pos[1]))
