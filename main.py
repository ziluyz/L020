import weapons
import monsters

class Fighter:
    def __init__(self, weapon: weapons.Weapon) -> None:
        self.weapon = weapon
        self.last_monster = None

    def change_weapon(self, weapon: weapons.Weapon):
        self.weapon = weapon
        print(f"Changed weapon to {self.weapon.name()}")

    def attack(self, monster: monsters.Monster):
        self.last_monster = monster
        self.attack_again()

    def attack_again(self):
        if self.last_monster is not None:
            self.last_monster.get_attacked(self.weapon.attack())
        else:
            print("No monster to attack")
    
player = Fighter(weapons.Bow())
player.attack(monsters.Ogre())
player.attack_again()
player.change_weapon(weapons.Sword())
player.attack(monsters.Ogre())
player.attack(monsters.Goblin())
player.change_weapon(weapons.Bow())
player.attack_again()
player.attack(monsters.Ghost())
player.attack_again()
player.change_weapon(weapons.Sword())
player.attack_again()
player.attack_again()