# Tuple Methods
# Tuples are immutable data structures

example_tuple = ('hello', 'hi', 'salutations', 'hi', 'ni hao', 'konnichiwa', 'hallo', 'hi')

# .count() - counts how many of the specified item there are within the tuple
print(f'.count() counts how many of an item exist in a tuple. The example contains: {example_tuple.count("hi")} "hi"s\n')

# .index() - returns the index of the first matching item, but can also be given an optional start index and end index
print(f'If we use .index on the whole tuple, the index returned is {example_tuple.index("hi")} for "hi"')
print(f'If we use .index starting at index 2, the index returned is {example_tuple.index("hi", 2)} for "hi"')
print(f'If we use .index starting at index 2 and ending at index 5, the index returned is {example_tuple.index("hi", 2, 5)} for "hi"\n')