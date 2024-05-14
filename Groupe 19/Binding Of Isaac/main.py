import pygame
from sys import exit
from Menu_button import Button
import time
from Hero import Hero
from Mob_spawn import ADDMOB, add_mob, mobs

pygame.init()

width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
background = pygame.image.load("assets/Graphics/background.png")
background = pygame.transform.scale(background, (width, height))


pygame.display.set_caption("Binding of Isaac")



fps = pygame.time.Clock()
pause = False
font = pygame.font.Font('assets/font/Hammer God Font DEMO.ttf', 36)




# def pause_handling(screen, font):
#     global pause
#
#     MOUSE_POS = pygame.mouse.get_pos()
#     # Create the text
#     text = font.render("Game paused : press Escape to resume", True, 'black')
#     text_rect = text.get_rect(center=(width/2, height/2 - 100))
#     screen.blit(text, text_rect)
#
#     # Create the buttons
#     resume_button = Button(image=None, pos=(width/2, height/2), text_input="Resume", font=font, base_color="Black", hovering_color="Green")
#     save_button = Button(image=None, pos=(width/2, height/2 + 100), text_input="Save", font=font, base_color="Black", hovering_color="Green")
#     quit_button = Button(image=None, pos=(width/2, height/2 + 200), text_input="Quit", font=font, base_color="Black", hovering_color="Green")
#
#     # Draw the buttons
#     mouse_pos = pygame.mouse.get_pos()
#     for button in [resume_button, save_button, quit_button]:
#         button.changeColor(mouse_pos)
#         button.update(screen)
#
#     # Check for mouse events
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if resume_button.checkForInput(MOUSE_POS):
#                 pause = not pause
#                 print("Resume game 1")
#             if save_button.checkForInput(MOUSE_POS):
#                 print("Save game functionality to be implemented")
#             if quit_button.checkForInput(MOUSE_POS):
#                 pygame.quit()
#
#     pygame.display.update()

hero = Hero("Entitys/Mobs/Hero/hero.json")
all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

def game(screen, font, pause=False):
    original_screen = screen.copy()  # Make a copy of the original screen
    pause_bg = None
    screenshot_taken = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                pass
            # Add a mob when the timer event occurs
            if event.type == ADDMOB:
                add_mob()
        #         if event.key == pygame.K_ESCAPE:
        #             pause = not pause
        #             if pause:
        #                 if not screenshot_taken:
        #                     pygame.image.save(screen, "pause.png")
        #                     screenshot_taken = True
        #                     pause_bg = pygame.image.load("pause.png").convert_alpha()
        #                     pause_bg_gs = pygame.Surface(pause_bg.get_size())
        #                     pygame.transform.grayscale(pause_bg, pause_bg_gs)
        #                     pygame.mixer.music.pause()
        #                 screen.blit(pause_bg_gs, (0, 0))
        #             else:
        #                 pygame.mixer.music.unpause()
        #                 screenshot_taken = False
        #
        # # Blit other elements onto the screen here
        #
        # if pause:
        #     pause_handling(screen, font)  # Draw pause menu
        # else:
        #     # Restore the original screen when unpaused
        #     screen.blit(original_screen, (0, 0))

        screen.blit(background, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        # Draw all the mobs
        for mob in mobs:
            mob.draw(screen)

        pygame.display.update()

        fps.tick(120)

# Start the game
game(screen, font, pause=False)