import pygame
from sys import exit
from Menu_button import Button

width, height = 1280, 720

pygame.init()


screen = pygame.display.set_mode((width, height))
screen.fill("white")
surface = pygame.Surface((width, height), pygame.SRCALPHA)
pygame.display.set_caption("Binding of Isaac")
pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)


fps = pygame.time.Clock()
pause = False
font = pygame.font.Font('assets/font/The walking font.ttf', 36)




def pause_handling(screen, surface, font):
    global pause
    # Create the text
    text = font.render("Game paused : press Escape to resume", True, 'black')
    text_rect = text.get_rect(center=(width/2, height/2 - 100))
    surface.blit(text, text_rect)

    # Create the buttons
    resume_button = Button(image=None, pos=(width/2, height/2), text_input="Resume", font=font, base_color="Black", hovering_color="Green")
    save_button = Button(image=None, pos=(width/2, height/2 + 100), text_input="Save", font=font, base_color="Black", hovering_color="Green")
    quit_button = Button(image=None, pos=(width/2, height/2 + 200), text_input="Quit", font=font, base_color="Black", hovering_color="Green")

    # Draw the buttons
    mouse_pos = pygame.mouse.get_pos()
    for button in [resume_button, save_button, quit_button]:
        button.changeColor(mouse_pos)
        button.update(screen)

    # Check for mouse events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if resume_button.checkForInput(mouse_pos):
                pause = False
                print("Resume game 1")
            elif save_button.checkForInput(mouse_pos):
                print("Save game functionality to be implemented")
            elif quit_button.checkForInput(mouse_pos):
                pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Resume game")
                pause = False


    # Blit the surface onto the screen
    screen.blit(surface, (0, 0))

    pygame.display.update()


def game(screen, surface, font, pause=False):
    original_screen = screen.copy()  # Make a copy of the original screen
    pauseBg = None
    screenshot_taken = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = not pause
                    if pause:
                        if not screenshot_taken:
                            pygame.image.save(screen, "pause.png")
                            screenshot_taken = True
                            pauseBg = pygame.image.load("pause.png").convert_alpha()
                            pauseBgGs = pygame.Surface(pauseBg.get_size())
                            pygame.transform.grayscale(pauseBg, pauseBgGs)
                            pygame.mixer.music.pause()
                        screen.blit(pauseBgGs, (0, 0))
                    else:
                        pygame.mixer.music.unpause()
                        screenshot_taken = False

        # Blit other elements onto the screen here

        if pause:
            pause_handling(screen, surface, font)  # Draw pause menu

        pygame.display.update()

        # Restore the original screen when unpaused
        if not pause:
            screen.blit(original_screen, (0, 0))

        fps.tick(120)

# Start the game
game(screen, surface, font, pause)