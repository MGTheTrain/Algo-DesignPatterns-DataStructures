#include <iostream>
#include <memory>
#include <mutex>

/**
 * @brief The Singleton class represents a class of which only one instance can exist.
 */
class Singleton {
public:
    /**
     * @brief Method to retrieve the singleton instance.
     * 
     * @return std::shared_ptr<Singleton> The singleton instance.
     */
    static std::shared_ptr<Singleton> getInstance() {
        std::lock_guard<std::mutex> lock(mutex_);
        if (!instance) {
            instance = std::make_shared<Singleton>();
        }
        return instance;
    }

    /**
     * @brief Method to display a message indicating the creation of the singleton instance.
     */
    void showMessage() {
        std::cout << "Singleton instance created!" << std::endl;
    }

private:
    /**
     * @brief Private constructor to prevent instantiation of Singleton.
     */
    Singleton() {}

    static std::shared_ptr<Singleton> instance; /**< The singleton instance. */
    static std::mutex mutex_; /**< Mutex for thread safety. */
};

std::shared_ptr<Singleton> Singleton::instance = nullptr; /**< Initialize the singleton instance. */
std::mutex Singleton::mutex_; /**< Initialize the mutex for thread safety. */

/**
 * @brief The main function demonstrates the use of the Singleton pattern.
 * 
 * @return int Program exit status
 */
int main() {
    std::shared_ptr<Singleton> singleton = Singleton::getInstance();
    singleton->showMessage();

    return 0;
}