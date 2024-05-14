import pygame
from sys import exit

pygame.init()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()