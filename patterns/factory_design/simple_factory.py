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


class Factory:

    def create_burger(self,type):
        if(type=="basic"):
            return BasicBurger()
        
        elif type=="standard":
            return StandardBurger()
        
        elif type=="premium":
            return PremiumBurger()
        

if __name__ == "__main__":
    burger_type= input("which burger type you want")

    factory= Factory()
    burger=factory.create_burger(burger_type)
    burger.prepare()

