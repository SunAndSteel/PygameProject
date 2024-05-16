import pygame
import math

screen = pygame.display.set_mode((1280, 720))


class Weapon:
    '''
    Classe Weapon : Classe représentant les armes du jeu
    '''
    def __init__(self, damage, cooldown):
        self.damage = damage
        self.cooldown = cooldown
        self.last_fire_time = pygame.time.get_ticks()

    def can_fire(self):
        '''
        Méthode pour vérifier si l'arme peut tirer
        '''
        current_time = pygame.time.get_ticks()
        return current_time - self.last_fire_time >= self.cooldown

    def fire(self, hero, mobs):
        '''
        methode pour faire tirer l'arme
        '''
        pass

    def draw(self, screen, x, y , image_path):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (30, 30))
        screen.blit(image, (x,y))

class Knife(Weapon):
    '''
    Classe Knife : Classe représentant le couteau du jeu
    '''
    def __init__(self):
        super().__init__(damage=20, cooldown=1000)

class Sword(Weapon):
    '''
    Classe Sword : Classe représentant l'épée du jeu
    '''
    def __init__(self):
        super().__init__(damage=30, cooldown=1500)

class Bullet:
    '''
    Classe Bullet : Classe représentant les balles tirées par le pistolet
    '''
    def __init__(self, start_pos, target_pos, damage):
        self.pos = list(start_pos)
        self.target = list(target_pos)
        self.speed = 10
        self.damage = damage
        direction = [self.target[0] - self.pos[0], self.target[1] - self.pos[1]]
        length = math.sqrt(direction[0]**2 + direction[1]**2)
        self.direction = [direction[0]/length, direction[1]/length]
        self.image = pygame.image.load('assets/Graphics/Projectiles/bullet.png')
        self.image = pygame.transform.scale(self.image, (30, 30))

    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed

    def intersects(self, mob):
        '''
        Méthode pour vérifier si la balle est en collision avec un mob
        '''
        return mob.rect.collidepoint(self.pos[0], self.pos[1])

    def draw(self, screen):
        screen.blit(self.image, (self.pos[0], self.pos[1]))

class Gun(Weapon):
    '''
    Classe Gun : Classe représentant le pistolet du jeu
    '''
    def __init__(self):
        super().__init__(damage=34, cooldown=500)
        self.bullets = []

    def fire(self, hero, mobs):
        '''
        Méthode pour faire tirer le pistolet
        '''
        if self.can_fire():
            mouse_pos = pygame.mouse.get_pos()
            bullet = Bullet(hero.rect.center, mouse_pos, self.damage)
            self.bullets.append(bullet)
            self.last_fire_time = pygame.time.get_ticks()

    def update(self, screen, mobs):
        for bullet in self.bullets:
            bullet.update()
            bullet.draw(screen)
            for mob in mobs:
                if bullet.intersects(mob):
                    mob.hurt(self.damage, mobs)
                    self.bullets.remove(bullet)
                    break
