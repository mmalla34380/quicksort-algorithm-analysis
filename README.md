# Quicksort Comparison Report

## Project Overview

This project evaluates the performance of two different quicksort implementations:

- **Deterministic Quicksort**: Always selects the first element as the pivot.
- **Randomized Quicksort**: Selects a pivot randomly from the list.

The objective is to observe and compare the behavior of both algorithms under different input conditions and input sizes.

## Input Types

The algorithms are tested with three types of input arrays:

1. **Random**: Unsorted list with randomly generated numbers.
2. **Sorted**: Pre-sorted list in ascending order.
3. **Reversed**: List sorted in descending order.

These cases are chosen to reflect best, average, and worst-case scenarios for the deterministic quicksort, which is sensitive to input order.

## Input Sizes Tested

- 1,000 elements
- 5,000 elements
- 10,000 elements

## Observations

- **Deterministic Quicksort** performs well on random data but suffers in performance and risks stack overflow on sorted or reversed inputs.
- **Randomized Quicksort** maintains consistent performance across all types of inputs due to random pivot selection.


## Issues Encountered

- For large, already sorted or reversed lists, the deterministic quicksort can exceed Python's recursion limit due to its unbalanced partitioning.
- A `RecursionError` was triggered during deterministic quicksort on sorted input with 5,000+ elements.

## Conclusion

Randomized quicksort is more robust and scalable for larger or ordered datasets. Deterministic quicksort is simple but sensitive to input structure, making it suitable only for small or random inputs unless optimized with techniques like median-of-three pivoting or tail recursion.

## Future Improvements

- Implement iterative quicksort to avoid recursion depth limits.
- Add memory usage profiling.
- Visualize sorting time via charts for better understanding.

## Requirements

- Python 3.x

## How to Run

1. Place the `compare_quicksort.py`, `deterministic_quicksort.py`, and `randomized_quicksort.py` in the same directory.
2. Run `compare_quicksort.py` to view performance comparison results.

