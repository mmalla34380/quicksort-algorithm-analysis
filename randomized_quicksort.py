import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    middle = [x for i, x in enumerate(arr) if x == pivot]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Example
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Sorted array (Randomized):", randomized_quicksort(arr))
