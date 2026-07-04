from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def get_abilities(self) -> str:
        pass


class Mario(Character):
    def get_abilities(self) -> str:
        return "Mario"
    

class CharacterDecorator(Character):
    def __init__(self, character: Character):
        self._character = character



class FireMario(CharacterDecorator):
    def get_abilities(self) -> str:
        return f"FireMario({self._character.get_abilities()})"
    

class SuperMario(CharacterDecorator):
    def get_abilities(self) -> str:
        return f"SuperMario({self._character.get_abilities()})"
    

class InvincibleMario(CharacterDecorator):
    def get_abilities(self) -> str:
        return f"InvincibleMario({self._character.get_abilities()})"
    
class FlyingMario(CharacterDecorator):
    def get_abilities(self) -> str:
        return f"FlyingMario({self._character.get_abilities()})"
    


if __name__ == "__main__":
    mario = Mario()
    print(mario.get_abilities())

    fire_mario = FireMario(mario)
    print(fire_mario.get_abilities())

    super_mario = SuperMario(fire_mario)
    print(super_mario.get_abilities())

    invincible_mario = InvincibleMario(super_mario)
    print(invincible_mario.get_abilities())

    flying_mario = FlyingMario(invincible_mario)
    print(flying_mario.get_abilities())


    fire_flying_mario = FlyingMario(FireMario(mario))
    print(fire_flying_mario.get_abilities())