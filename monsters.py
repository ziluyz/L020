from abc import ABC, abstractmethod

class Monster(ABC):
    @abstractmethod
    def get_attacked(strength: int):
        pass

class MonsterWithHP(Monster):
    def get_attacked(self, strength: int):
        if self.hitpoints <= 0:
            print(f"{self.name} is already dead\n")
            return
        print(f"{self.name} is attacked with strength {strength}")
        self.hitpoints -= strength
        if self.hitpoints <= 0:
            print(f"{self.name} died")
        else:
            print(f"Remaining hitpoints: {self.hitpoints}")
        print()

class Goblin(MonsterWithHP):
    def __init__(self) -> None:
        self.name = "Goblin"
        self.hitpoints = 5

class Ogre(MonsterWithHP):
    def __init__(self) -> None:
        self.name = "Ogre"
        self.hitpoints = 10

class Ghost(Monster):
    def __init__(self) -> None:
        self.active = True
    def get_attacked(self, strength: int):
        if not self.active:
            print("Ghost is already eliminated\n")
            return
        print(f"Ghost is attacked with strength {strength}")
        if strength > 5:
            self.active = False
            print(f"Ghost is eliminated")
        else:
            print(f"Nothing happened")
        print()