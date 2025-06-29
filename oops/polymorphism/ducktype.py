class Duck:
    def quack(self):
        print("Quack quack")

class Person:
    def quack(self):
        print("I can mimic a duck")

def make_it_quack(entity):
    entity.quack()

d = Duck()
d = Person()

make_it_quack(Duck())  # Quack quack
make_it_quack(d)  # I can mimic a duck
if __name__ == '__main__':
    print("This script is being run directly.")
    make_it_quack(d)
    make_it_quack(d)