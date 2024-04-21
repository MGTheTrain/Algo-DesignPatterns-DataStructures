def heapify(arr, n, i):
    """
    Heapify subtree rooted at index i.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Heap sort algorithm.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def main_heap_sort():
    """
    Main entry point for heap sort.
    """
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print("Sorted array:", arr)


if __name__ == "__main__":
    main_heap_sort()
