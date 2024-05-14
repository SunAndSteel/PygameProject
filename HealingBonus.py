import Bonus
import Hero 

class HealingBonus(Bonus):
    def __init__(self):
        super().__init__()
        self.heal_obtained = 10


    def healing(self, hero:Hero):
        Hero.health += self.heal_obtained