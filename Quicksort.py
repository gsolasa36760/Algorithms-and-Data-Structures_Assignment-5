"""The Quicksort algorithm selects a pivot, partitions the array into smaller and greater elements, and recursively sorts
the subarrays. This process continues until the array is fully sorted.
"""

# Implementing the Quicksort algorithm
def quicksort(arr):
    # Checking if the array has one or zero elements
    if len(arr) <= 1:
        return arr

    # Selecting the last element as the pivot
    pivot = arr[-1]

    # Partitioning the array into two parts based on the pivot
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]

    # Recursively sorting the two partitions and combining the results
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# Testing the quicksort function with an example
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
