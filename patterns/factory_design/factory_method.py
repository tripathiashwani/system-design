from abc import ABC, abstractmethod

class Burger(ABC):

    @abstractmethod
    def prepare():
        pass


class BasicBurger(Burger):

    def prepare(self):
        print("preparing basic burger")

class StandardBurger(Burger):

    def prepare(self):
        print("preparing standard burger")



class PremiumBurger(Burger):

    def prepare(self):
        print("preparing Premium burger")




class BasicWheatBurger(Burger):

    def prepare(self):
        print("preparing wheat basic burger")

class StandardWheatBurger(Burger):

    def prepare(self):
        print("preparing wheat standard burger")



class PremiumWheatBurger(Burger):

    def prepare(self):
        print("preparing wheat Premium burger")


class Factory(ABC):
    @abstractmethod
    def create_burger(self,type):
        pass


class SinghBurger(Factory):

    def create_burger(self, type):
        if(type=="basic"):
            return BasicBurger()
        
        elif type=="standard":
            return StandardBurger()
        
        elif type=="premium":
            return PremiumBurger()
        


class KingBurger(Factory):

    def create_burger(self, type):
        if(type=="basic"):
            return BasicWheatBurger()
        
        elif type=="standard":
            return StandardWheatBurger()
        
        elif type=="premium":
            return PremiumWheatBurger()

if __name__ == "__main__":
    burger_type= input("which burger type you want")

    factory= KingBurger()
    burger=factory.create_burger(burger_type)
    burger.prepare()

