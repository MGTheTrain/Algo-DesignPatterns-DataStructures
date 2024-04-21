from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def execute(self):
        """Abstract method representing the execution of a service."""
        pass

class Client:
    def __init__(self, service):
        """
        Constructor for the Client class.

        Args:
            service (Service): The service to be used by the client.
        """
        self.service = service

    def do_something(self):
        """Performs an action using the provided service."""
        self.service.execute()

class ConcreteService(Service):
    def execute(self):
        """Concrete implementation of the service execution."""
        print("Executing ConcreteService")

def main():
    # Create a concrete service
    service = ConcreteService()
    # Create a client with the concrete service
    client = Client(service)
    # Perform an action using the service
    client.do_something()

if __name__ == "__main__":
    main()
