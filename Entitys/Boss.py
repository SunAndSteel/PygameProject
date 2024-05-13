import pygame
from Entitys.Entity import Entity

HAUTEUR, LARGEUR = 800, 800
screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
clock = pygame.time.Clock()





class Boss(Entity):
    def __init__(self, fury_mode, resistance, mouvements, path):
        super().__init__(path)
        self.fury_mode = fury_mode
        self.resistance = resistance
        self.mouvements = mouvements

    def update(self):
        super().update()
        if self.mouvements == "up-down":
            self.rect.y += self.speed
            if self.rect.top < 0 or self.rect.bottom > HAUTEUR:
                self.speed = -self.speed  # Inverser la direction lorsque le boss atteint les bords de l'écran
        elif self.mouvements == "left-right":
            self.rect.x += self.speed
            if self.rect.left < 0 or self.rect.right > LARGEUR:
                self.speed = -self.speed  # Inverser la direction lorsque le boss atteint les bords de l'écran

    def show_informations(self):
        super().show_informations()
        if self.show_player_information:
            info_surface = pygame.Surface((200, 50))
            info_surface.fill((0, 0, 0))
            info = [
                f"Nom: {self.name}",
                f"Santé: {self.health}/{self.max_health}"
            ]
            font = pygame.font.SysFont("Arial", 20)
            for i, text in enumerate(info):
                text_render = font.render(text, True, (255, 255, 255))
                info_surface.blit(text_render, (10, 10 + i * 20))
            screen.blit(info_surface, (self.rect.centerx - info_surface.get_width() // 2, self.rect.top - 30))


boss = Boss("Entitys/Mobs/Boss/boss.json")
all_sprites = pygame.sprite.Group()
all_sprites.add(boss)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()