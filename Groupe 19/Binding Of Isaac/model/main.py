from RoomView import RoomView
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
r = RoomView()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    r.draw_from_matrix(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
