#include <iostream>
#include <memory>

/**
 * @brief The Service interface declares a method for executing a service.
 */
class Service {
public:
    virtual void execute() const = 0;

    /**
     * @brief Virtual destructor to allow proper destruction of derived classes
     */
    virtual ~Service() = default;
};

/**
 * @brief The Client class depends on the Service interface, not concrete
 * implementations.
 */
class Client {
private:
    std::unique_ptr<Service> service; /**< Pointer to the Service object */

public:
    /**
     * @brief Construct a new Client object with the provided Service.
     * 
     * @param s Unique pointer to the Service object
     */
    Client(std::unique_ptr<Service> s) : service(std::move(s)) {}

    /**
     * @brief Performs an action using the provided Service.
     */
    void doSomething() const {
        service->execute();
    }
};

/**
 * @brief The ConcreteService class provides a concrete implementation of the
 * Service interface.
 */
class ConcreteService : public Service {
public:
    /**
     * @brief Executes the concrete service.
     */
    void execute() const override {
        std::cout << "Executing ConcreteService\n";
    }
};

/**
 * @brief The main function demonstrates the use of the Dependency Inversion
 * Principle (DIP) in SOLID.
 * 
 * @return int Program exit status
 */
int main() {
    std::unique_ptr<Service> service = std::make_unique<ConcreteService>();
    std::unique_ptr<Client> client = std::make_unique<Client>(std::move(service));
    client->doSomething();
    return 0;
}
