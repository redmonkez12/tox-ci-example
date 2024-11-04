import random


class Weapon:
    def __init__(self, strength, endurance, width, height, health):
        self.strength = strength
        self.endurance = endurance
        self.width = width
        self.height = height
        self.health = health

    def attack(self):
        if self.health < 10:
            raise Exception("Nemuzu utocit")
            # return 0

        value = random.randint(0, self.endurance)  # 10 Nahodny prvek 1

        # 10 < 30 / 2 = 10 < 15
        if value < (self.endurance // 2):
            self.health -= 1

        bonus_damage = random.randint(0, 20)  # 10 Nahodny prvek 2

        return self.strength + bonus_damage
