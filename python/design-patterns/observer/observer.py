from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        """Method called by the Subject when its state changes."""
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        """Attaches an observer to the subject."""
        self.observers.append(observer)

    def detach(self, observer):
        """Detaches an observer from the subject."""
        self.observers.remove(observer)

    def notify(self, message):
        """Notifies all observers when the subject's state changes."""
        for observer in self.observers:
            observer.update(message)

class ConcreteObserver1(Observer):
    def update(self, message):
        """Prints a message upon receiving an update from the Subject."""
        print("ConcreteObserver1 received message:", message)

class ConcreteObserver2(Observer):
    def update(self, message):
        """Prints a message upon receiving an update from the Subject."""
        print("ConcreteObserver2 received message:", message)

def main():
    # Create a subject
    subject = Subject()

    # Create observers
    observer1 = ConcreteObserver1()
    observer2 = ConcreteObserver2()

    # Attach observers to the subject
    subject.attach(observer1)
    subject.attach(observer2)

    # Notify observers
    subject.notify("Hello Observers!")

    # Detach observer2
    subject.detach(observer2)

    # Notify observers again
    subject.notify("Observers, are you there?")

if __name__ == "__main__":
    main()
