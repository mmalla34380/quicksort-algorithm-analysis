import time
import random
from deterministic_quicksort import quicksort
from randomized_quicksort import randomized_quicksort

def generate_inputs(size):
    return {
        'Random': [random.randint(0, 10000) for _ in range(size)],
        'Sorted': list(range(size)),
        'Reversed': list(range(size, 0, -1))
    }

def test_sorting_algorithms():
    sizes = [1000, 5000, 10000]
    for size in sizes:
        print(f"\nInput Size: {size}")
        inputs = generate_inputs(size)
        for desc, arr in inputs.items():
            arr_copy1 = arr[:]
            arr_copy2 = arr[:]

            start = time.time()
            quicksort(arr_copy1)
            dt = time.time() - start

            start = time.time()
            randomized_quicksort(arr_copy2)
            rt = time.time() - start

            print(f"{desc} - Deterministic: {dt:.4f}s, Randomized: {rt:.4f}s")

if __name__ == "__main__":
    test_sorting_algorithms()
