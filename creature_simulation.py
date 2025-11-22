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

<<<<<<< HEAD
class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power, altitude=0):
        super().__init__(name, hp, attack_power)
        self.altitude = altitude

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude}m.")

    def attack(self, target):
        print(f"{self.name} dives from {self.altitude}m to strike {target.name}!")
=======
class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power, depth=0):
        super().__init__(name, hp, attack_power)
        self.depth = depth

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth}m.")

    def attack(self, target):
        print(f"{self.name} lunges underwater at {target.name}!")
>>>>>>> swimming_creature
        target.hp -= self.attack_power
