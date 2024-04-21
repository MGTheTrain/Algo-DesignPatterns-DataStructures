from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        """Abstract method representing the operation."""
        pass

class ConcreteComponent(Component):
    def operation(self):
        """Concrete implementation of the operation."""
        print("ConcreteComponent operation")

class Decorator(Component):
    def __init__(self, component: Component):
        """
        Constructor for the Decorator class.

        Args:
            component (Component): The component to be decorated.
        """
        self.component = component

    def operation(self):
        """Delegates the operation to the wrapped component."""
        self.component.operation()

class ConcreteDecorator(Decorator):
    def operation(self):
        """Overrides the operation to add additional behavior."""
        super().operation()  # Calls the wrapped component's operation
        print("Added behavior in ConcreteDecorator")

class AnotherConcreteDecorator(Decorator):
    def operation(self):
        """Overrides the operation to add different behavior."""
        super().operation()  # Calls the wrapped component's operation
        print("Added behavior in AnotherConcreteDecorator")

class AnotherConcreteDecorator2(Decorator):
    def operation(self):
        """Overrides the operation to add another behavior."""
        super().operation()  # Calls the wrapped component's operation
        print("Added behavior in AnotherConcreteDecorator2")

def main():
    component = ConcreteComponent()
    decorated = ConcreteDecorator(component)
    decorated.operation()

    print("\n")

    another_decorated = AnotherConcreteDecorator(decorated)
    another_decorated.operation()

    print("\n")

    another_decorated2 = AnotherConcreteDecorator2(another_decorated)
    another_decorated2.operation()

if __name__ == "__main__":
    main()
