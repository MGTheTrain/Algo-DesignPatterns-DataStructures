class Node:
    def __init__(self, data):
        """
        Node class represents each element in the doubly linked list.
        """
        self.data = data  # Data stored in the node
        self.prev = None  # Reference to the previous node
        self.next = None  # Reference to the next node

class DoublyLinkedList:
    def __init__(self):
        """
        DoublyLinkedList class represents the doubly linked list data structure.
        """
        self.head = None  # Reference to the head node
        self.tail = None  # Reference to the tail node
        self.size = 0  # Number of elements in the list

    def __len__(self):
        """
        Returns the number of elements in the list.
        """
        return self.size

    def __getitem__(self, index):
        """
        Returns the element at the specified index.
        """
        if not 0 <= index < self.size:
            raise IndexError('Index out of bounds')
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def insert_at(self, index, item):
        """
        Inserts an element at the specified index.
        """
        if not 0 <= index <= self.size:
            raise IndexError('Index out of bounds')
        new_node = Node(item)
        if index == 0:
            # Insertion at the beginning
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        elif index == self.size:
            # Insertion at the end
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            # Insertion at a specific index
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
        self.size += 1

    def remove_at(self, index):
        """
        Removes the element at the specified index.
        """
        if not 0 <= index < self.size:
            raise IndexError('Index out of bounds')
        if index == 0:
            # Removal from the beginning
            if self.size == 1:
                # Special case: list has only one element
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.size - 1:
            # Removal from the end
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            # Removal from a specific index
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1

def main():
    """
    Main entry point.
    """
    dll = DoublyLinkedList()
    dll.insert_at(0, 1)
    dll.insert_at(1, 2)
    dll.insert_at(2, 3) # insertion between
    dll.insert_at(2, 5) # insertion between
    dll.insert_at(2, 7) # insertion between
    print("Length of the doubly linked list: ", len(dll))
    print("Element at index 0: ", dll[0])
    print("Element at index 1: ", dll[1])
    print("Element at index 2: ", dll[2])
    print("Element at index 3: ", dll[3])
    print("Element at index 4: ", dll[4])
    dll.remove_at(1)
    dll.remove_at(3)
    print("Length of the doubly linked list after removal: ", len(dll))
    print("Element at index 0: ", dll[0])
    print("Element at index 1: ", dll[1])
    print("Element at index 1: ", dll[2])

if __name__ == "__main__":
    main()
