from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self):
        """Abstract method to execute the strategy."""
        pass

class ConcreteStrategy1(Strategy):
    def execute(self):
        """Executes the first concrete strategy."""
        print("Executing ConcreteStrategy1")

class ConcreteStrategy2(Strategy):
    def execute(self):
        """Executes the second concrete strategy."""
        print("Executing ConcreteStrategy2")

class Context:
    def __init__(self, strategy):
        """
        Initializes the context with a strategy.

        Args:
            strategy (Strategy): The strategy to be used.
        """
        self._strategy = strategy

    def setStrategy(self, strategy):
        """
        Sets a new strategy for the context.

        Args:
            strategy (Strategy): The new strategy to be set.
        """
        self._strategy = strategy

    def executeStrategy(self):
        """Executes the current strategy."""
        self._strategy.execute()

def main():
    # Create instances of concrete strategies
    strat1 = ConcreteStrategy1()
    strat2 = ConcreteStrategy2()

    # Create a context with the first strategy and execute it
    context = Context(strat1)
    context.executeStrategy()

    # Change the strategy to the second one and execute it
    context.setStrategy(strat2)
    context.executeStrategy()

if __name__ == "__main__":
    main()
