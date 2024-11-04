class Barbarian:
    def __init__(self, strength, stamina, weapon):
        self.strength = strength
        self.stamina = stamina
        self.weapon = weapon

    def attack(self):
        weapon_attack = self.weapon.attack() + self.strength # 20 + 60

        # 80 > 15 and 60 > 50 and 100 > 30
        if weapon_attack > 15 and self.strength > 50 and self.stamina > 30:
            weapon_attack += 10

        return weapon_attack