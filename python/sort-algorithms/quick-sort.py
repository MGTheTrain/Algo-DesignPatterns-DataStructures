def partition(arr, low, high):
    """
    Partition the array using the last element as pivot.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    """
    Quick sort algorithm.
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def main_quick_sort():
    """
    Main entry point for quick sort.
    """
    arr = [12, 11, 13, 5, 6, 7]
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)


if __name__ == "__main__":
    main_quick_sort()
