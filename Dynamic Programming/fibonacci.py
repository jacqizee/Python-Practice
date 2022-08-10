memo = {}

def fibonacci(num: int) -> int:
    # no negative numbers
    if num < 0:
        return

    # base case
    if num <= 1:
        memo[num] = num
    
    # recursive case
    if num in memo:
        return memo[num]
    else:
        memo[num] = fibonacci(num - 1) + fibonacci(num - 2)

    return memo[num]