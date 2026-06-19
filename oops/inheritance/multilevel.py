# Multilevel Inheritance Example in Python

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

# Usage
d = Dog()
d.speak()  # Inherited from Animal
d.walk()   # Inherited from Mammal
d.bark()   # Defined in Dog