import pygame
from model.Room import Room

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    r = Room(1)
    r.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
