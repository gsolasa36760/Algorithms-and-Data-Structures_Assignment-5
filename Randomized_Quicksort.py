"""Implementing the randomized Quicksort algorithm selects a random pivot, partitions the array around it, and recursively sorts the subarrays.
Swapping the pivot with the last element ensures efficient partitioning, improving performance by reducing the likelihood of worst-case behavior.
"""

import random


# Randomized Quicksort algorithm implementation
def randomized_quicksort(arr):
    # Base case: if the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choosing a random pivot index
    pivot_index = random.randint(0, len(arr) - 1)
    # Swapping the randomly selected pivot with the last element
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]

    # Pivot selection: using the last element after randomization
    pivot = arr[-1]

    # Partitioning the array into elements less than or equal to pivot and greater than pivot
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]

    # Recursively sorting both subarrays
    return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_pivot)


# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = randomized_quicksort(arr)
print("Sorted array:", sorted_arr)
