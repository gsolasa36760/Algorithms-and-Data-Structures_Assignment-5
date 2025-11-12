"""Implementing the iterative Quicksort algorithm uses a stack to simulate recursion and partition the array around a pivot.
Randomly selecting the pivot helps avoid deep recursion, improving performance for large arrays.
"""

import random
import time


# Implementing the iterative Quicksort algorithm
def iterative_quicksort(arr):
    # Initializing the stack with the first and last indices
    stack = [(0, len(arr) - 1)]

    # Processing the stack until it is empty
    while stack:
        # Popping the subarray range from the stack
        low, high = stack.pop()

        # Checking if the subarray has more than one element
        if low < high:
            # Partitioning the array and getting the pivot index
            pivot_index = partition(arr, low, high)

            # Adding the left subarray to the stack
            stack.append((low, pivot_index - 1))
            # Adding the right subarray to the stack
            stack.append((pivot_index + 1, high))

    # Returning the sorted array
    return arr


# Implementing the partition function used by iterative_quicksort
def partition(arr, low, high):
    # Selecting the pivot as the last element in the array
    pivot = arr[high]
    # Initializing the pointer for the smaller elements
    i = low - 1

    # Iterating over the array to rearrange elements around the pivot
    for j in range(low, high):
        # Swapping elements smaller than the pivot with the left side
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Placing the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Returning the index of the pivot
    return i + 1


# Implementing the randomized iterative Quicksort algorithm
def randomized_iterative_quicksort(arr):
    # Initializing the stack with the first and last indices
    stack = [(0, len(arr) - 1)]

    # Processing the stack until it is empty
    while stack:
        # Popping the subarray range from the stack
        low, high = stack.pop()

        # Checking if the subarray has more than one element
        if low < high:
            # Randomly selecting a pivot and swapping it with the last element
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

            # Partitioning the array and getting the pivot index
            pivot_index = partition(arr, low, high)

            # Adding the left subarray to the stack
            stack.append((low, pivot_index - 1))
            # Adding the right subarray to the stack
            stack.append((pivot_index + 1, high))

    # Returning the sorted array
    return arr


# Defining a helper function to measure the time taken for sorting
def measure_time(sort_func, arr):
    # Recording the start time
    start_time = time.time()
    # Sorting the array using the provided sorting function
    sort_func(arr)
    # Returning the elapsed time
    return time.time() - start_time


# Running the analysis for different input distributions
input_sizes = [1000, 5000, 10000]
distributions = ['random', 'sorted', 'reverse_sorted']

# Running the tests for different input sizes and distributions
for n in input_sizes:
    print(f"Testing for input size {n}:")

    for dist in distributions:
        # Generating the input array based on the distribution
        if dist == 'random':
            arr = random.sample(range(n), n)
        elif dist == 'sorted':
            arr = list(range(n))
        elif dist == 'reverse_sorted':
            arr = list(range(n, 0, -1))

        # Measuring the time for deterministic iterative quicksort
        time_det = measure_time(iterative_quicksort, arr[:])
        print(f"  Iterative Quicksort ({dist}): {time_det:.5f} seconds")

        # Measuring the time for randomized iterative quicksort
        time_rand = measure_time(randomized_iterative_quicksort, arr[:])
        print(f"  Randomized Iterative Quicksort ({dist}): {time_rand:.5f} seconds")

    print()
