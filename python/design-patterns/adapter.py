from abc import ABC, abstractmethod

class Target(ABC):
    """Interface for the client to interact with."""
    @abstractmethod
    def request(self):
        """Abstract method to be implemented by concrete classes."""
        pass

class Adaptee:
    """Contains some useful behavior with an incompatible interface."""
    def specific_request(self):
        """Method representing the specific request of the Adaptee."""
        print("Adaptee's specific request")

class Adapter(Target):
    """Adapts the interface of Adaptee to the Target interface."""
    def __init__(self, adaptee: Adaptee):
        """Initialize the Adapter with an instance of Adaptee."""
        self.adaptee = adaptee

    def request(self):
        """Implement the request method to bridge between Target and Adaptee."""
        self.adaptee.specific_request()

def main():
    """Entry point of the program."""
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.request()

if __name__ == "__main__":
    main()
