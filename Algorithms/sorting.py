def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    pass

def selection_sort(arr):
    pass

def merge_sort(arr):
    pass

def quick_sort(arr):
    pass

def radix_sort(arr):
    pass