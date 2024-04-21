import threading

class Singleton:
    _instance = None  # Private static variable to hold the singleton instance
    _lock = threading.Lock()  # Lock for thread safety

    @staticmethod
    def getInstance():
        """
        Static method to retrieve the singleton instance.
        
        Returns:
            Singleton: The singleton instance.
        """
        if Singleton._instance is None:  
            with Singleton._lock:  # Acquire the lock for thread safety
                if Singleton._instance is None:  # Double check to ensure thread safety
                    print("Singleton instance created")
                    Singleton._instance = Singleton()  
        return Singleton._instance  

    def printMessage(self):
        """Method to print a test message."""
        print("Test...")

def threadFunc():
    """Function to be executed by each thread."""
    singleton = Singleton.getInstance()  
    singleton.printMessage()  

def main():
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=threadFunc))  
    
    for thread in threads:
        thread.start()  

    for thread in threads:
        thread.join()  

if __name__ == "__main__":
    main()
