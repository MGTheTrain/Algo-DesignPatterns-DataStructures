#include <iostream>
#include <memory>

/**
 * @note Adheres Single Responsibility Principle (SRP) in SOLID
 */

/**
 * @brief The Component interface declares the operation method.
 */
class Component {
public:
    virtual void operation() const = 0;

    /**
     * @brief Virtual destructor to allow proper destruction of derived classes
     */
    virtual ~Component() = default;
};

/**
 * @brief The ConcreteComponent class defines an object to which additional
 * responsibilities can be attached.
 */
class ConcreteComponent : public Component {
public:
    void operation() const override {
        std::cout << "ConcreteComponent operation\n";
    }
};

/**
 * @brief The Decorator class maintains a reference to a Component object and
 * defines an interface that conforms to Component's interface.
 */
class Decorator : public Component {
protected:
    std::shared_ptr<Component> component; /**< Pointer to the Component object */

public:
    /**
     * @brief Construct a new Decorator object with the provided Component.
     * 
     * @param comp Pointer to the Component object
     */
    Decorator(std::shared_ptr<Component> comp) : component(comp) {}

    /**
     * @brief Passes the operation request to the wrapped Component.
     */
    void operation() const override {
        component->operation();
    }
};

/**
 * @brief The ConcreteDecorator class adds responsibilities to the component.
 */
class ConcreteDecorator : public Decorator {
public:
    /**
     * @brief Construct a new ConcreteDecorator object with the provided Component.
     * 
     * @param comp Pointer to the Component object
     */
    ConcreteDecorator(std::shared_ptr<Component> comp) : Decorator(comp) {}

    /**
     * @brief Executes the operation of the wrapped Component and adds behavior.
     */
    void operation() const override {
        Decorator::operation();
        addedBehavior();
    }

    /**
     * @brief Provides additional behavior in ConcreteDecorator.
     */
    void addedBehavior() const {
        std::cout << "Added behavior in ConcreteDecorator\n";
    }
};

/**
 * @brief AnotherConcreteDecorator adds more responsibilities to the component.
 */
class AnotherConcreteDecorator : public Decorator {
public:
    /**
     * @brief Construct a new AnotherConcreteDecorator object with the provided Component.
     * 
     * @param comp Pointer to the Component object
     */
    AnotherConcreteDecorator(std::shared_ptr<Component> comp) : Decorator(comp) {}

    /**
     * @brief Executes the operation of the wrapped Component and adds more behavior.
     */
    void operation() const override {
        Decorator::operation();
        addedBehavior();
    }

    /**
     * @brief Provides additional behavior in AnotherConcreteDecorator.
     */
    void addedBehavior() const {
        std::cout << "Added behavior in AnotherConcreteDecorator\n";
    }
};

/**
 * @brief The main function demonstrates the use of the Decorator pattern.
 * 
 * @return int Program exit status
 */
int main() {
    std::shared_ptr<Component> component = std::make_shared<ConcreteComponent>();
    std::shared_ptr<Component> decorated = std::make_shared<ConcreteDecorator>(component);
    decorated->operation();

    std::cout << "\n";

    std::shared_ptr<Component> anotherDecorated = std::make_shared<AnotherConcreteDecorator>(decorated);
    anotherDecorated->operation();

    return 0;
}