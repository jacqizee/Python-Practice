def selection_sort(arr):
    for i in range(len(arr)):
        pointer = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[pointer]:
                pointer = j
        arr[i], arr[pointer] = arr[pointer], arr[i]
    return arr