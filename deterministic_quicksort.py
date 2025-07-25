def quicksort(arr):
    if len(arr) <= 1:
        return arr

    mid_index = len(arr) // 2
    pivot = arr[mid_index]
    
    # Exclude the pivot index to prevent infinite recursion when all elements are equal
    left = [x for i, x in enumerate(arr) if x < pivot or (x == pivot and i < mid_index)]
    middle = [x for x in arr if x == pivot]
    right = [x for i, x in enumerate(arr) if x > pivot or (x == pivot and i > mid_index)]

    return quicksort(left) + middle + quicksort(right)

# Example
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Sorted array (Deterministic):", quicksort(arr))
