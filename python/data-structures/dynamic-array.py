import ctypes

# implementation from: https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/

class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''

    def __init__(self):
        """
        Initializes the dynamic array.
        """
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Returns the number of elements stored in the array.
        """
        return self.n

    def __getitem__(self, k):
        """
        Returns the element at index k.
        """
        if not 0 <= k < self.n:
            raise IndexError('Index out of bounds')
        return self.A[k]

    def append(self, ele):
        """
        Adds an element to the end of the array.
        """
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = ele 
        self.n += 1

    def insert_at(self, item, index):
        """
        Inserts an item at the specified index.
        """
        if not 0 <= index <= self.n:
            raise IndexError('Index out of bounds')
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i-1]
        self.A[index] = item
        self.n += 1

    def remove_at(self, index):
        """
        Removes the item at the specified index.
        """
        if not 0 <= index < self.n:
            raise IndexError('Index out of bounds')
        for i in range(index, self.n-1):
            self.A[i] = self.A[i+1]
        self.A[self.n-1] = 0
        self.n -= 1

    def _resize(self, new_cap):
        """
        Resizes the internal array to the new capacity new_cap.
        """
        B = self.make_array(new_cap)
        B[:self.n] = self.A[:self.n]
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        """
        Returns a new array with capacity new_cap.
        """
        return (new_cap * ctypes.py_object)()

def main():
    """
    Main entry point.
    """
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print("Length of the array: ", len(arr))
    print("Element at index 0: ", arr[0])
    print("Element at index 1: ", arr[1])
    print("Element at index 2: ", arr[2])
    arr.remove_at(1)
    print("Length of the array: ", len(arr))
    print("Element at index 0: ", arr[0])
    print("Element at index 1: ", arr[1])

if __name__ == "__main__":
    main()
