#include <iostream>
#include <memory>
#include <mutex>
#include <thread>
#include <vector>

/**
 * @brief The Product class represents the complex object being constructed.
 */
class Product {
public:
    /**
     * @brief Method to add a part to the product.
     * 
     * @param part The part to add.
     */
    void addPart(const std::string& part) {
        std::lock_guard<std::mutex> lock(mutex_);
        parts += part + ", ";
    }

    /**
     * @brief Method to display the parts of the product.
     */
    void showParts() {
        std::lock_guard<std::mutex> lock(mutex_);
        std::cout << "Product parts: " << parts << std::endl;
    }

private:
    std::string parts;
    std::mutex mutex_;
};

/**
 * @brief The Builder interface declares methods for creating parts of a complex object.
 */
class Builder {
public:
    virtual ~Builder() {}

    /**
     * @brief Method to build part A.
     */
    virtual void buildPartA() = 0;

    /**
     * @brief Method to build part B.
     */
    virtual void buildPartB() = 0;

    /**
     * @brief Method to retrieve the constructed product.
     * 
     * @return std::shared_ptr<Product> The constructed product.
     */
    virtual std::shared_ptr<Product> getProduct() = 0;
};

/**
 * @brief The ConcreteBuilder class implements the Builder interface to construct a specific product.
 */
class ConcreteBuilder : public Builder {
public:
    /**
     * @brief Constructor to initialize the product.
     */
    ConcreteBuilder() : product(std::make_shared<Product>()) {}

    /**
     * @brief Method to build part A.
     */
    void buildPartA() override {
        product->addPart("Part A");
    }

    /**
     * @brief Method to build part B.
     */
    void buildPartB() override {
        product->addPart("Part B");
    }

    /**
     * @brief Method to retrieve the constructed product.
     * 
     * @return std::shared_ptr<Product> The constructed product.
     */
    std::shared_ptr<Product> getProduct() override {
        return product;
    }

private:
    std::shared_ptr<Product> product;
};

/**
 * @brief The Director class is responsible for using the builder to construct a complex object.
 */
class Director {
public:
    /**
     * @brief Method to set the builder to use.
     * 
     * @param builder The builder to set.
     */
    void setBuilder(std::shared_ptr<Builder> builder) {
        this->builder = builder;
    }

    /**
     * @brief Method to construct the product using the assigned builder.
     */
    void construct() {
        builder->buildPartA();
        builder->buildPartB();
    }

private:
    std::shared_ptr<Builder> builder;
};

int main() {
    std::shared_ptr<Builder> builder = std::make_shared<ConcreteBuilder>();
    Director director;
    director.setBuilder(builder);

    std::vector<std::thread> threads;

    auto threadFunc = [&director, &builder]() {
        director.construct();
        std::shared_ptr<Product> product = builder->getProduct();
        product->showParts();
    };

    for (int i = 0; i < 5; ++i) {
        threads.emplace_back(threadFunc);
    }

    for (auto& thread : threads) {
        thread.join();
    }

    return 0;
}
