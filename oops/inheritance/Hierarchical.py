class Animal:
    def eat(self):
        print("Animal eats food.")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks on land.")

class Dog(Mammal):
    def bark(self):
        print("Dog barks.")

# Example usage
d = Dog()
d.eat()    # Inherited from Animal
d.walk()   # Inherited from Mammal
d.bark()   # Defined in Dog