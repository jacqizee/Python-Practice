# Radix sorts by grouping numbers by digits place, rather than comparing numbers against one another
# aka a non-comparison sort

def radix_sort(arr: 'list[int]'):
    digits = len(str(max(arr)))
    being_sorted = arr[:]

    for i in range(digits):
        holder = [[] for digit in range(10)]
        index = -(i + 1)
        for num in being_sorted:
            num_as_str = str(num)
            try:
                holder[int(num_as_str[index])].append(num)
            except:
                holder[0].append(num)
        being_sorted = []
        for digits_place in holder:
            being_sorted += digits_place
    
    return being_sorted