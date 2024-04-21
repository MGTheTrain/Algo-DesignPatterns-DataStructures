#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>

/**
 * @brief The Observer interface declares the update method, which is called by
 * the Subject when its state changes.
 */
class Observer {
public:
    virtual void update(const std::string& message) = 0;

    /**
     * @brief Virtual destructor to allow proper destruction of derived classes
     */
    virtual ~Observer() = default;
};

/**
 * @brief The Subject interface declares methods for attaching, detaching, and
 * notifying observers.
 */
class Subject {
private:
    std::vector<std::shared_ptr<Observer>> observers;

public:
    /**
     * @brief Attaches an observer to the subject.
     * 
     * @param observer Shared pointer to the observer object
     */
    void attach(const std::shared_ptr<Observer>& observer) {
        observers.push_back(observer);
    }

    /**
     * @brief Detaches an observer from the subject.
     * 
     * @param observer Shared pointer to the observer object
     */
    void detach(const std::shared_ptr<Observer>& observer) {
        auto it = std::find_if(observers.begin(), observers.end(), [&](const auto& obs) {
            return obs.get() == observer.get();
        });
        if (it != observers.end()) {
            observers.erase(it);
        }
    }


    /**
     * @brief Notifies all observers when the subject's state changes.
     * 
     * @param message Message to be sent to observers
     */
    void notify(const std::string& message) {
        for (const auto& observer : observers) {
            observer->update(message);
        }
    }
};

/**
 * @brief ConcreteObserver1 implements the update method to react to state
 * changes in the Subject.
 */
class ConcreteObserver1 : public Observer {
public:
    /**
     * @brief Prints a message upon receiving an update from the Subject.
     * 
     * @param message Message received from the Subject
     */
    void update(const std::string& message) override {
        std::cout << "ConcreteObserver1 received message: " << message << std::endl;
    }
};

/**
 * @brief ConcreteObserver2 implements the update method to react to state
 * changes in the Subject.
 */
class ConcreteObserver2 : public Observer {
public:
    /**
     * @brief Prints a message upon receiving an update from the Subject.
     * 
     * @param message Message received from the Subject
     */
    void update(const std::string& message) override {
        std::cout << "ConcreteObserver2 received message: " << message << std::endl;
    }
};

/**
 * @brief The main function demonstrates the use of the Observer pattern.
 * 
 * @return int Program exit status
 */
int main() {
    Subject subject;

    auto observer1 = std::make_shared<ConcreteObserver1>();
    auto observer2 = std::make_shared<ConcreteObserver2>();

    subject.attach(observer1);
    subject.attach(observer2);

    subject.notify("Hello Observers!");

    subject.detach(observer2);

    subject.notify("Observers, are you there?");

    return 0;
}