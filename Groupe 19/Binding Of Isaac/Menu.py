"""
Ce module contient le menu principal du jeu. Il comprend des options pour jouer au jeu, changer de difficulté et quitter le jeu.
"""
import pygame, sys
from Menu_button import Button
import random
from main import *

# Initialiser pygame
pygame.init()

# Load les musiques
music_files = ["assets/Sound/Menu song.mp3","assets/Sound/Menu song.mp3","assets/Sound/Menu song.mp3","assets/Sound/Menu song 2.mp3"]
music = random.choice(music_files)
pygame.mixer.music.load(music)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# Set up the display
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# Load le background
BG = pygame.image.load("assets/Graphics/Background_menu.jpg")

# Mettre la difficulté
difficulty = 'NORMAL'

# Fonction pour avoir le font
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font/The walking font.ttf", size)

# fonction pour jouer
def play():
    """
        Commence le jeu. Il comprend également une option pour revenir au menu principal.
    """
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# fonction pour les options
def options():
    """
    Fournit des options pour choisir la difficulté du jeu. Il comprend également une option pour revenir au menu principal.
    """
    global difficulty
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Choose your game difficulty", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_EASY = Button(image=None, pos=(200, 360),
                             text_input="EASY", font=get_font(75), base_color="Black",hovering_color='Grey', selected=difficulty=='EASY')
        OPTIONS_NORMAL = Button(image=None, pos=(640, 360),
                               text_input="NORMAL", font=get_font(75), base_color="Black",hovering_color='Grey', selected=difficulty=='NORMAL')
        OPTIONS_HARD = Button(image=None, pos=(1080, 360),
                             text_input="HARD", font=get_font(75), base_color="Black",hovering_color="Grey", selected=difficulty=='HARD')
        OPTIONS_BACK = Button(image=None, pos=(640, 650),
                              text_input="GO BACK", font=get_font(75), base_color="Black", hovering_color="Grey")

        # Update la couleur de base selon si le bouton est sélectionné ou non
        OPTIONS_EASY.base_color = "Grey" if OPTIONS_EASY.selected else "Black"
        OPTIONS_NORMAL.base_color = "Grey" if OPTIONS_NORMAL.selected else "Black"
        OPTIONS_HARD.base_color = "Grey" if OPTIONS_HARD.selected else "Black"

        mouse_pos = pygame.mouse.get_pos()
        for button in [OPTIONS_BACK, OPTIONS_EASY, OPTIONS_NORMAL, OPTIONS_HARD]:
            button.changeColor(mouse_pos)  # Changer la couleur du bouton si la souris est dessus
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_EASY.checkForInput(OPTIONS_MOUSE_POS):
                    difficulty = 'EASY'
                    OPTIONS_EASY.selected = True
                    OPTIONS_NORMAL.selected = False
                    OPTIONS_HARD.selected = False
                if OPTIONS_NORMAL.checkForInput(OPTIONS_MOUSE_POS):
                    difficulty = 'NORMAL'
                    OPTIONS_EASY.selected = False
                    OPTIONS_NORMAL.selected = True
                    OPTIONS_HARD.selected = False
                if OPTIONS_HARD.checkForInput(OPTIONS_MOUSE_POS):
                    difficulty = 'HARD'
                    OPTIONS_EASY.selected = False
                    OPTIONS_NORMAL.selected = False
                    OPTIONS_HARD.selected = True

        pygame.display.update()

# Fonction pour le menu principal
def main_menu():
    """
    Affiche le menu principal du jeu. Il comprend des options pour jouer au jeu, changer de difficulté et quitter le jeu.
    """
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Graphics/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Graphics/Options Rect.png"), pos=(640, 400),
                                text_input="DIFFICULTY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Graphics/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                    music.stop()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Start the game
main_menu()