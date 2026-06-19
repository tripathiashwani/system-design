class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal (single inheritance)
    def bark(self):
        print("Dog barks")

# Usage
dog = Dog()
dog.speak()  # Inherited method from Animal
dog.bark()   # Method from Dog