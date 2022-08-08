dictionary = {
    'apple': 'a red fruit that is common in pies',
    'strawberry': 'a red pseudo-berry fruit that is tart and sweet',
    'avocado': 'a green, creamy fruit that is great on toast'
}

# ? .copy() returns a shallow copy of a dictionary
copied_dict = dictionary.copy()
print(f'This is a shallow dict copy: {copied_dict}\n')

# ? .fromkeys() creates a dictionary from the given keys and value
keys = { 'apple', 'banana', 'pear' }
value = 'fruit'
new_dict = dict.fromkeys(keys, value)
print(f'This is a new dict created with .fromkeys(), which all have the same value: {new_dict}\n')

# ? .get() returns the value of a specified key
apple_description = dictionary.get('apple')
print(f"We can use get to get the KVP values. Apple's value is: '{apple_description}'\n")

# ? .items() returns a list containing tuples of KVPs in the dict
print(f'Dictionary into KVP tuples: {dictionary.items()}\n')

# ? .keys() returns a list of all keys in a dict as a dict_keys object
print(f'.keys() returns a list of keys for a given dict: {dictionary.keys()}\n')

# ? .popitem() removes and returns the last KVP inserted into the dictionary
last_item = dictionary.popitem()
print(f'.popitem() removes and returns the last KVP added to the dict: {last_item}\nDictionary: {dictionary}\n')

# ? .setdefault() returns the value of a key if it exists, otherwise adds it to the dict with specified value
print(f'.setdefault() gets or sets the value of a key depending on if it exists in the dict.\nBefore: {dictionary} \nUsing getdefault(): {dictionary.setdefault("banana", "a yellow fruit that is curvy")}\nAfter: {dictionary}')

# ? .pop() removes and returns the value with the given key
print(f'.pop() removes and returns a value when given a specified key. For example, we can remove banana: {dictionary.pop("banana")}\nAfter: {dictionary}')

# ? .values() returns a list of values in the dictionary
print(f'The values in the example dict are: {dictionary.values()}')

# ? .clear() clears a dictionary
dictionary.clear()
print(f'An empty dictionary: {dictionary}')