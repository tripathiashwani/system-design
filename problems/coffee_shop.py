from abc import ABC, abstractmethod
from typing import Dict, Type, List


class Coffee(ABC):

    def __init__(self,initial_price:int):
        self.price=initial_price
        

    @abstractmethod
    def get_taste(self):
        pass

    def get_price(self):
        return self.price

    


class Espresso(Coffee):
    def get_taste(self):
        return "Espresso"
    

class Latte(Coffee):
    def get_taste(self):
        return "Latte"
    

class Cappuccino(Coffee):
    def get_taste(self):
        return "Cappuccino"
    

class CoffeeDecorator(Coffee):

    def __init__(self,coffee:Coffee,price:int):
        self.coffee:Coffee=coffee
        self.price:int=price

    @abstractmethod
    def get_taste(self):
        pass

    def get_price(self):
        return self.price+self.coffee.get_price()


class Milk(CoffeeDecorator):
        
    def get_taste(self):
        return f"Milk({self.coffee.get_taste()})"
    

    
    
    

class Caramel(CoffeeDecorator):
    
    def get_taste(self):
        return f"Caramel({self.coffee.get_taste()})"
    
        
    


class ChocolateSyrup(CoffeeDecorator):
    
    def get_taste(self):
        return f"Chocolate({self.coffee.get_taste()})"
    

    


if __name__ == "__main__":
    espresso=Espresso(10)
    print(espresso.get_taste())
    print(espresso.get_price())


    chocolate_espresso=ChocolateSyrup(espresso,5)
    print(chocolate_espresso.get_taste())
    print(chocolate_espresso.get_price())


    choco_caramel_espresso=Caramel(chocolate_espresso,4)
    print(choco_caramel_espresso.get_taste())
    print(choco_caramel_espresso.get_price())