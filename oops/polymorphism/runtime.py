class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
a.speak()      # Animal speaks

d = Dog()
d.speak()      # Dog barks

if __name__ == '__main__':
    print("This script is being run directly.")
    a.speak()
    d.speak()