class HashTable:
    def __init__(self, size):
        """
        Initializes the hash table with the given size.
        """
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """
        Hashes the key to an index in the table.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.
        """
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def search(self, key):
        """
        Searches for a key in the hash table and returns its value.
        If the key is not found, returns None.
        """
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def remove(self, key):
        """
        Removes a key-value pair from the hash table.
        """
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, _) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    if len(self.table[index]) == 0:
                        self.table[index] = None  # Reset to None if the list is empty
                    return
        return None


def main():
    """
    Main entry point.
    """
    hash_table = HashTable(10)
    hash_table.insert("slow", 5)
    hash_table.insert("cold", 7)
    hash_table.insert("strong", 3)
    hash_table.insert("brave", 4)

    print("Value for 'slow':", hash_table.search("slow"))
    print("Value for 'cold':", hash_table.search("cold"))
    print("Value for 'strong':", hash_table.search("strong"))
    print("Value for 'brave':", hash_table.search("brave"))

    hash_table.remove("cold")
    print("Value for 'cold' after removal:", hash_table.search("cold"))
if __name__ == "__main__":
    main()
