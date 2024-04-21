import threading

class Product:
    """Represents the complex object being constructed."""
    def __init__(self):
        self.parts = []
        self.mutex = threading.Lock()

    def add_part(self, part):
        """Method to add a part to the product."""
        with self.mutex:
            self.parts.append(part)

    def show_parts(self):
        """Method to display the parts of the product."""
        with self.mutex:
            print("Product parts:", ", ".join(self.parts))

class Builder:
    """Interface for creating parts of a complex object."""
    def build_part_a(self):
        """Method to build part A."""
        raise NotImplementedError

    def build_part_b(self):
        """Method to build part B."""
        raise NotImplementedError

    def get_product(self):
        """Method to retrieve the constructed product."""
        raise NotImplementedError

class ConcreteBuilder(Builder):
    """Implements the Builder interface to construct a specific product."""
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        """Method to build part A."""
        self.product.add_part("Part A")

    def build_part_b(self):
        """Method to build part B."""
        self.product.add_part("Part B")

    def get_product(self):
        """Method to retrieve the constructed product."""
        return self.product

class Director:
    """Responsible for using the builder to construct a complex object."""
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct(self):
        """Method to construct the product using the assigned builder."""
        self.builder.build_part_a()
        self.builder.build_part_b()

def main():
    """Entry point of the program."""
    builder = ConcreteBuilder()
    director = Director(builder)

    threads = []

    def thread_func():
        """Function to be executed by each thread."""
        director.construct()
        product = builder.get_product()
        product.show_parts()

    for _ in range(5):
        t = threading.Thread(target=thread_func)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()