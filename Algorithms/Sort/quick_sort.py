import random

# Quick Sort - pivot can be selected a number of ways (ex. random, first pos, last pos, etc.)
# Sorts in place, so no arr is returned

def quick_sort(arr, start, end):
    # Base Case
    if start >= end:
        return

    pivot = random.randrange(start, end + 1)
    pivot_value = arr[pivot]
    arr[end], arr[pivot] = arr[pivot], arr[end]

    pointer = start
    for i in range(start, end):
        if arr[i] < pivot_value:
            arr[pointer], arr[i] = arr[i], arr[pointer]
            pointer += 1
    arr[pointer], arr[end] = arr[end], arr[pointer]

    quick_sort(arr, start, pointer - 1)
    quick_sort(arr, pointer + 1, end)