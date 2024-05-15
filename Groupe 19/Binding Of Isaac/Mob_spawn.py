import pygame
from random import randint, randrange, choice
from Mob import Mob
from Obstacle import *
from Boss import Boss

pygame.init()

# Add a timer for adding mobs


mobs = []
obstacles = []
screen = pygame.display.set_mode((1280, 720))


mini_hitler = pygame.image.load("assets/Graphics/Mobs/minihitler.png").convert_alpha()
mini_hitler = pygame.transform.scale(mini_hitler, (100, 100))
Soldier = pygame.image.load("assets/Graphics/Mobs/solider.png").convert_alpha()
Soldier = pygame.transform.scale(Soldier, (100, 100))
Gazeur = pygame.image.load("assets/Graphics/Mobs/gazeur.png").convert_alpha()
Gazeur = pygame.transform.scale(Gazeur, (100, 100))

unheal = pygame.image.load("assets/Graphics/malus/grave.png").convert_alpha()
unheal = pygame.transform.scale(unheal, (100, 100))
heal = pygame.image.load("assets/Graphics/bonus/diamond.png").convert_alpha()
heal = pygame.transform.scale(heal, (100, 100))
speed = pygame.image.load("assets/Graphics/bonus/mushroom.png").convert_alpha()
speed = pygame.transform.scale(speed, (100, 100))
shield = pygame.image.load("assets/Graphics/bonus/shield.png").convert_alpha()
shield = pygame.transform.scale(shield, (100, 100))
Rage = pygame.image.load("assets/Graphics/bonus/Piment.png").convert_alpha()
Rage = pygame.transform.scale(Rage, (100, 100))

Caporal_boss = pygame.image.load("assets/Graphics/Boss/caporal.png").convert_alpha()
Caporal_boss = pygame.transform.scale(Caporal_boss, (200, 200))
Hitler_boss = pygame.image.load("assets/Graphics/Boss/hitler.png").convert_alpha()
Hitler_boss = pygame.transform.scale(Hitler_boss, (200, 200))


def add_obstacle(hero, max_obstacles=2):
    global obstacles
    min_distance_from_hero = 200  # Minimum distance from hero


    obstacle_images_effects = [(heal, 'heal'), (speed, 'speed'), (shield, 'shield'), (Rage, 'rage'), (unheal, 'unheal')]
    obstacle_image, obstacle_effect = choice(obstacle_images_effects)
    obstacle_x, obstacle_y = randint(0, screen.get_width()), randint(0, screen.get_height())

    if ((obstacle_x - hero.rect.x) ** 2 + (obstacle_y - hero.rect.y) ** 2) ** 0.5 < min_distance_from_hero:
        return

    obstacle = Obstacle(obstacle_image, obstacle_x, obstacle_y,obstacle_effect )

    if (any(obstacle.intersects(other_obstacle) for other_obstacle in obstacles) or any(obstacle.intersects(other_mob)
                                                                                        for other_mob in mobs) or
            obstacle.rect.right >= 1280 or obstacle.rect.bottom >= 720 or obstacle.rect.left < 0 or obstacle.rect.top < 0):
        return

    obstacles.append(obstacle)
    obstacle.draw(screen)  # Draw the obstacle on the screen


def add_mob(hero):
    global mobs

    entry_point = (1280,400)
    min_distance_from_entry = 500  # Minimum distance from entry point
    min_distance_from_hero = 200  # Minimum distance from hero

    mob_image = choice([mini_hitler, Soldier, Gazeur])
    mob_x, mob_y = randint(0, screen.get_width()), randint(0, screen.get_height())

    # Check the distance from the hero
    if ((mob_x - hero.rect.x) ** 2 + (mob_y - hero.rect.y) ** 2) ** 0.5 < min_distance_from_hero:
        return

    if ((mob_x - entry_point[0]) ** 2 + (mob_y - entry_point[1]) ** 2) ** 0.5 < min_distance_from_entry:
        return

    mob = Mob(mob_image, mob_x, mob_y, hero)

    if (any(mob.intersects(other_mob) for other_mob in mobs) or any(mob.intersects(other_obstacle)
                                                                   for other_obstacle in obstacles) or
            mob.rect.right >= 1280 or mob.rect.bottom >= 720 or mob.rect.left < 0 or mob.rect.top < 0):
        return

    mobs.append(mob)
    mob.draw(screen)  # Draw the mob on the screen

def add_boss(hero):
    global mobs

    boss = choice([Caporal_boss, Hitler_boss])
    boss_x, boss_y = randint(0, screen.get_width()), randint(0, screen.get_height())

    boss = Boss(boss, boss_x, boss_y, hero)

    print("Boss added")
    mobs.append(boss)
    boss.draw(screen)



