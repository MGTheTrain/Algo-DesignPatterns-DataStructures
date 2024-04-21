#include <iostream>
#include <memory>
#include <mutex>
#include <thread>
#include <vector>

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
            instance = std::shared_ptr<Singleton>(new Singleton);
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
    static std::shared_ptr<Singleton> instance; 
    static std::mutex mutex_; 
};

std::shared_ptr<Singleton> Singleton::instance = nullptr; 
std::mutex Singleton::mutex_; 

int main() {
    std::vector<std::thread> threads;
    auto threadFunc = []() {  // Lambda function to be executed by each thread
        std::shared_ptr<Singleton> singleton = Singleton::getInstance();
        singleton->showMessage();
    };
    for (int i = 0; i < 5; ++i) {
        threads.emplace_back(threadFunc);
    }
    for (auto& thread : threads) {
        thread.join();
    }
    return 0;
}