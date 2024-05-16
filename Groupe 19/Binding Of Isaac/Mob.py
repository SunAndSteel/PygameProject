from Boss import Boss
from Hero import *
from Projectile import Projectile

mort = False

class Mob(Boss):
    def __init__(self, image, x, y, target,Id=2 ):
        super().__init__(image, x, y, target)
        self.__health = 100
        self.__level = 50
        self.__Id = Id
        self.__x = x
        self.__y = y
        self.__target = target
        self.__image = image
        self.__rect = self.image.get_rect(topleft=(x, y))
        self.__last_attack_time = pygame.time.get_ticks()


    def constant_pos(self):
        return [self.rect.x, self.rect.y]

    def hurt(self, damage, mobs):
        self.health -= damage
        print(f"Mob health: {self.health}")
        if self.health <= 0:
            self.kill(mobs)

    def shoot(self):
        from main import projectiles
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 3000:
            projectile = Projectile(self.rect.center, self.target.rect.center , 'assets/Graphics/Projectiles/gaz.png' if self.Id == 2 else 'assets/Graphics/Projectiles/gammedcross.png')
            projectiles.add(projectile)
            self.last_attack_time = current_time

    def kill(self, mobs):
        # from main import dropped_weapons
        # random_number = 2
        # if random_number == 2:
        #     second_random_number = 0
        #     if second_random_number == 0:
        #         from Weapons import Gun
        #         weapon = Gun()
        #         weapon.pos = [self.rect.x, self.rect.y]
        #         weapon.image_path = "assets/Graphics/Weapons/gun.png"
        #         dropped_weapons.append(weapon)
        #         print("j'ai dessiné un gun")
        #     elif second_random_number == 1:
        #         pass
        #     elif second_random_number == 2:
        #         pass
        if self in mobs:
            mobs.remove(self)
        super().kill()

    def update(self):
        if self.Id == 2 or self.Id == 3:
            self.shoot()
        if self.Id == 1:
            if self.rect.colliderect(self.target.rect):
                current_time = pygame.time.get_ticks()
                if current_time - self.last_attack_time >= 1000:
                    self.target.hurt(10)
                    self.last_attack_time = current_time

        super().update()

    def intersects(self, other):
        return self.rect.colliderect(other.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    # def is_dead(self):
    #     global mort
    #     if self.health <= 0:
    #         mort = True

    def show_informations(self):
        super().show_informations()
        if self.show_player_information:
            info_surface = pygame.Surface((200, 50))
            info_surface.fill((0, 0, 0))
            info = [
                f"Résistance: {self.resistance}",
                f"Deplacement: {self.deplacement}",
                f"Level: {self.level}"
            ]
            for i, text in enumerate(info):
                info_surface.blit(pygame.font.SysFont(None, 20).render(text, True, (255, 255, 255)), (10, i * 20))
            screen.blit(info_surface, (self.rect.x, self.rect.y - 50))
            pygame.display.flip()

