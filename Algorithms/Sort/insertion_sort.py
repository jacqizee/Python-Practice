def insertion_sort(arr):
    for i in range(1, len(arr)):
        pointer = i - 1
        while arr[i] < arr[pointer] and pointer >= 0:
            arr[pointer], arr[i] = arr[i], arr[pointer]
            pointer -= 1
            i -= 1
    return arr