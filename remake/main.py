import pygame
import remake.controllers.GameState as GameState

pygame.init()
screen = pygame.display.set_mode((1280, 720))

"""
L'objet 'Gamestate' évite de devoir intéragir avec des variables globales
ce qui devient ingérables quand on a plusieurs étages, maps, etc.

Il permet la réprésentation dynamique des états du jeu :
    - position dans la map
    - nombre de monstres dans la salle
    - temps de jeu
    - ...
"""
gamestate = GameState

while True:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()