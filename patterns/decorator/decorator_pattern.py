from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"
    

class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component
    
   

class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self._component.operation()})"
    

class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self._component.operation()})"
    


if __name__ == "__main__":
    component = ConcreteComponent()
    print(component.operation())

    decorator_a = ConcreteDecoratorA(component)
    print(decorator_a.operation())

    decorator_b = ConcreteDecoratorB(decorator_a)
    print(decorator_b.operation())

    decorator_ab=ConcreteDecoratorB(ConcreteDecoratorA(component))
    print(decorator_ab.operation())