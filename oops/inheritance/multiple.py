# Demonstrating multiple inheritance in Python with critical cases

# Base classes
class A:
    def __init__(self):
        print("A.__init__")
        self.value_a = "A"

    def method(self):
        print("A.method")

    def common(self):
        print("A.common")

class B:
    def __init__(self):
        print("B.__init__")
        self.value_b = "B"

    def method(self):
        print("B.method")

    def common(self):
        print("B.common")

# Multiple inheritance with diamond problem
class C(A, B):
    def __init__(self):
        print("C.__init__")
        super().__init__()  # Uses MRO, calls A.__init__
        self.value_c = "C"

    def method(self):
        print("C.method")
        super().method()  # Calls A.method due to MRO

    def common(self):
        print("C.common")
        super().common()  # Calls A.common due to MRO

# Another diamond shape
class D(B, A):
    def __init__(self):
        print("D.__init__")
        super().__init__()  # Uses MRO, calls B.__init__
        self.value_d = "D"

    def method(self):
        print("D.method")
        super().method()  # Calls B.method due to MRO

    def common(self):
        print("D.common")
        super().common()  # Calls B.common due to MRO

# Mixins and method resolution order
class Mixin:
    def mixin_method(self):
        print("Mixin.mixin_method")

class E(C, Mixin):
    def __init__(self):
        print("E.__init__")
        super().__init__()
        self.value_e = "E"

    def method(self):
        print("E.method")
        super().method()

# Ambiguous attribute access
class F(A, B):
    def __init__(self):
        print("F.__init__")
        A.__init__(self)
        B.__init__(self)
        self.value_f = "F"

    def method(self):
        print("F.method")
        A.method(self)
        B.method(self)

# Test cases
if __name__ == "__main__":
    print("\n--- Instance of C ---")
    c = C()
    c.method()
    c.common()
    print(c.value_a, c.value_c)

    print("\n--- Instance of D ---")
    d = D()
    d.method()
    d.common()
    print(d.value_b, d.value_d)

    print("\n--- Instance of E (with mixin) ---")
    e = E()
    e.method()
    e.mixin_method()
    print(e.value_a, e.value_c, e.value_e)

    print("\n--- Instance of F (explicit calls) ---")
    f = F()
    f.method()
    print(f.value_a, f.value_b, f.value_f)

    print("\n--- MROs ---")
    print("C MRO:", [cls.__name__ for cls in C.__mro__])
    print("D MRO:", [cls.__name__ for cls in D.__mro__])
    print("E MRO:", [cls.__name__ for cls in E.__mro__])
    print("F MRO:", [cls.__name__ for cls in F.__mro__])