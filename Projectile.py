import pygame

pygame.init()


class Projectile(pygame.sprite.Sprite):
    '''
    Classe Projectile : Classe représentant les projectiles tirés par les mobs
    '''
    def __init__(self, start_pos, target_pos,image):
        super().__init__()
        image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect(center=start_pos)
        self.direction = pygame.Vector2(target_pos) - self.rect.center  # Calcule la direction vers le joueur
        self.direction.normalize_ip()
        self.speed = 10

    def update(self):
        '''
        Méthode pour mettre à jour la position du projectile
        Supprime le projectile si il sort de l'écran
        '''
        self.rect.center += self.direction * self.speed
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)