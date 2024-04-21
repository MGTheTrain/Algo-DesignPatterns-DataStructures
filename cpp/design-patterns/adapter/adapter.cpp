#include <iostream>
#include <memory>

/**
 * @note Adheres Interface Segregation Principle (ISP) in SOLID
 */

/**
 * @brief The Target interface declares a method for the client to interact
 * with.
 */
class Target {
public:
    virtual void request() const = 0;

    /**
     * @brief Virtual destructor to allow proper destruction of derived classes
     */
    virtual ~Target() = default;
};

/**
 * @brief The Adaptee class contains some useful behavior, but its interface is
 * incompatible with the client code.
 */
class Adaptee {
public:
    /**
     * @brief Specific request that Adaptee can perform.
     */
    void specificRequest() const {
        std::cout << "Adaptee's specific request\n";
    }
};

/**
 * @brief The Adapter class implements the Target interface and bridges the gap
 * between Target and Adaptee.
 */
class Adapter : public Target {
private:
    std::unique_ptr<Adaptee> adaptee; /**< Pointer to the Adaptee object */

public:
    /**
     * @brief Construct a new Adapter object with a provided Adaptee.
     * 
     * @param a Pointer to the Adaptee object
     */
    Adapter(std::unique_ptr<Adaptee> a) : adaptee(std::move(a)) {}

    /**
     * @brief Requests a specific action from the Adaptee through the Adapter.
     */
    void request() const override {
        adaptee->specificRequest();
    }
};

/**
 * @brief The main function demonstrates the use of the Adapter pattern.
 * 
 * @return int Program exit status
 */
int main() {
    std::unique_ptr<Adaptee> adaptee = std::make_unique<Adaptee>();
    std::unique_ptr<Adapter> adapter = std::make_unique<Adapter>(std::move(adaptee));
    adapter->request();
    return 0;
}
