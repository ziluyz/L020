from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def attack(self) -> int:
        pass



class Sword(Weapon):
    def name(self):
        return "Sword"
    def attack(self):
        print("Sword attack")
        return 10

class Bow(Weapon):
    def name(self):
        return "Bow"
    def attack(self):
        print("Bow attack")
        return 5