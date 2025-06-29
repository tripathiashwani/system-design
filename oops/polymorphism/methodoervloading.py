#python handles methodoverloading at runtime, not at compile time.


class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))      
print(calc.add(2, 3, 4))   


class MathUtils:
    def multiply(self, *args):
        if len(args) == 2:
            a, b = args
            return a * b
        elif len(args) == 3:
            a, b, c = args
            return a * b * c
        else:
            raise TypeError("multiply expects 2 or 3 arguments")

m = MathUtils()
print(m.multiply(2, 3))       # 6
print(m.multiply(2, 3, 4))    # 24
print(m.multiply(2))          # raises TypeError

if __name__ == '__main__':
    print("This script is being run directly.")