def linear_search(arr: 'list[int]', target: int) -> int:
    for i, val in enumerate(arr):
        if val == target:
            return i
    return None