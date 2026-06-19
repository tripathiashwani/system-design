from abc import ABC, abstractmethod

class Burger(ABC):

    @abstractmethod
    def prepare():
        pass

class GarlicBread(ABC):

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



class BasicGarlicBread(GarlicBread):

    def prepare(self):
        print("preparing basic garlic bread")

class StandardGarlicBread(GarlicBread):

    def prepare(self):
        print("preparing standard  garlic bread")



class PremiumGarlicBread(GarlicBread):

    def prepare(self):
        print("preparing Premium garlic bread")


class BasicWheatBurger(Burger):

    def prepare(self):
        print("preparing wheat basic burger")

class StandardWheatBurger(Burger):

    def prepare(self):
        print("preparing wheat standard burger")



class PremiumWheatBurger(Burger):

    def prepare(self):
        print("preparing wheat Premium burger")




class BasicWheatGarlicBread(GarlicBread):

    def prepare(self):
        print("preparing wheat basic Garlic Bread")

class StandardWheatGarlicBread(GarlicBread):

    def prepare(self):
        print("preparing wheat standard Garlic Bread")



class PremiumWheatGarlicBread(GarlicBread):

    def prepare(self):
        print("preparing wheat Premium Garlic Bread")

class Factory(ABC):
    @abstractmethod
    def create_burger(self,type):
        pass

    @abstractmethod
    def create_garlic_bread(self,type):
        pass



class SinghBurger(Factory):

    def create_burger(self, type):
        if(type=="basic"):
            return BasicBurger()
        
        elif type=="standard":
            return StandardBurger()
        
        elif type=="premium":
            return PremiumBurger()
        
    

    def create_garlic_bread(self, type):
        if(type=="basic"):
            return BasicGarlicBread()
        
        elif type=="standard":
            return StandardGarlicBread()
        
        elif type=="premium":
            return PremiumGarlicBread()
        


class KingBurger(Factory):

    def create_burger(self, type):
        if(type=="basic"):
            return BasicWheatBurger()
        
        elif type=="standard":
            return StandardWheatBurger()
        
        elif type=="premium":
            return PremiumWheatBurger()
        
    
    def create_garlic_bread(self, type):
        if(type=="basic"):
            return BasicWheatGarlicBread()
        
        elif type=="standard":
            return StandardWheatGarlicBread()
        
        elif type=="premium":
            return PremiumWheatGarlicBread()

if __name__ == "__main__":
    burger_type= input("which burger type you want")
    garlic_bread_type= input("which garlic bread type you want")

    factory= KingBurger()
    burger=factory.create_burger(burger_type)
    garlic_bread=factory.create_garlic_bread(garlic_bread_type)
    burger.prepare()
    garlic_bread.prepare()

