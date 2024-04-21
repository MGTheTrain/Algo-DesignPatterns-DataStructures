#include <iostream>
#include <memory>

/**
 * @brief The Strategy interface declares a method for executing a strategy.
 */
class Strategy {
public:
    virtual void execute() const = 0;

    /**
     * @brief Virtual destructor to allow proper destruction of derived classes
     */
    virtual ~Strategy() = default;
};

/**
 * @brief The ConcreteStrategy1 class provides a concrete implementation of
 * Strategy.
 */
class ConcreteStrategy1 : public Strategy {
public:
    /**
     * @brief Executes the first concrete strategy.
     */
    void execute() const override {
        std::cout << "Executing ConcreteStrategy1\n";
    }
};

/**
 * @brief The ConcreteStrategy2 class provides another concrete implementation
 * of Strategy.
 */
class ConcreteStrategy2 : public Strategy {
public:
    /**
     * @brief Executes the second concrete strategy.
     */
    void execute() const override {
        std::cout << "Executing ConcreteStrategy2\n";
    }
};

/**
 * @brief The Context class contains a pointer to a Strategy object and
 * delegates the execution of the strategy to that object.
 */
class Context {
private:
    std::unique_ptr<Strategy> strategy;

public:
    /**
     * @brief Construct a new Context object with the provided Strategy.
     * 
     * @param strat Unique pointer to the Strategy object
     */
    Context(std::unique_ptr<Strategy> strat) : strategy(std::move(strat)) {}

    /**
     * @brief Sets a new Strategy for the Context.
     * 
     * @param strat Unique pointer to the new Strategy object
     */
    void setStrategy(std::unique_ptr<Strategy> strat) {
        strategy = std::move(strat);
    }

    /**
     * @brief Executes the current Strategy.
     */
    void executeStrategy() const {
        strategy->execute();
    }
};

/**
 * @brief The main function demonstrates the use of the Open/Closed Principle
 * (OCP) in SOLID.
 * 
 * @return int Program exit status
 */
int main() {
    std::unique_ptr<Strategy> strat1 = std::make_unique<ConcreteStrategy1>();
    std::unique_ptr<Strategy> strat2 = std::make_unique<ConcreteStrategy2>();

    std::unique_ptr<Context> context = std::make_unique<Context>(std::move(strat1));
    context->executeStrategy();

    context->setStrategy(std::move(strat2));
    context->executeStrategy();

    return 0;
}