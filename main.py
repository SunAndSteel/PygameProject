import pygame
from model.Room import Room

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
r = Room(1, 3)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    r.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
