# List Methods

animals = ['cats', 'dogs', 'fish', 'monkeys', 'sharks', 'elephants']

# ? index() - returns the index of an element, immutable
print(f'The index for dogs is: {animals.index("dogs")}')
print(f'The index for elepants is: {animals.index("elephants")}')

# ? append() - adds an item to a list, mutable
animals.append('birds')
animals.append('frogs')
print(f"Appended birds and frogs: {animals} \n")

# ? extend() - adds an iterable item to the end of a list, mutable
more_animals = ['whales', 'dolphins', 'zebras', 'horses']
animals.extend(more_animals)
print(f"Extended animals, adding 4 new animals: {animals} \n")

# ? insert() - inserts an item at the specified index, mutable
animals.insert(0, 'rats')
print(f"Inserted rats: \n {animals} \n")

# ? remove() - removes an item by value, mutable
animals.remove('rats')
print(f"Removed rats: {animals} \n")

# ? count() - counts how many of a certain value
print(f"There are {animals.count('rats')} rats \n")
print(f"There are {animals.count('cats')} cats \n")

# ? pop() - removes an element at a specified index (default is -1), returning the value, mutable
print(f"The last animal in animals was {animals.pop()} \n")
print(f"The first animal in animals was {animals.pop(0)} \n")
print(f"{animals} \n")

# ? reverse() - reverses the order of the list, mutable
animals.reverse()
print(f"Reversed animals: {animals} \n")

# ? sort() - sorts items in a list, default is in acending order. mutable. accepts key and reverse arguments
animals.sort(reverse=True)
print(f"Sorted animals by reverse alphabetical: \n {animals} \n")
animals.sort()
print(f"Sorted animals by alphabetical: \n {animals} \n")
animals.sort(key= lambda x: x[-1]) #this sorts the array using the last letter as the key
print(f"Sorted animals by last character: \n {animals} \n")

# ? copy() - returns a shallow copy of a list (aka creates a new list, but the items point to the same references initially), immutable
numbers = [1, 2, 3, 4, 5]
numbers_copy = numbers.copy()
print(f"Is the copy the same as the original list? {numbers is numbers_copy}")
print(f"Is the first number equal to the copied first number? {numbers[0] is numbers_copy[0]}")
numbers[0] = 5
print(f"Can we modify a number in the original without modifying the copy? {numbers[0] is not numbers_copy[0]} \n")

# ? enumerate() - transforms a list to a dict
print(f"This is an enumerated list: {dict(enumerate(animals))} \n")

# ? clear() - removes all elements within a list, mutable
animals.clear()
print(f"All animals are cleared from the list: {len(animals) == 0}")
