class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.hp -= self.attack_power

    def is_alive(self):
        return self.hp > 0

class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power, depth=0):
        super().__init__(name, hp, attack_power)
        self.depth = depth

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth}m.")

    def attack(self, target):
        print(f"{self.name} lunges underwater at {target.name}!")
        target.hp -= self.attack_power
