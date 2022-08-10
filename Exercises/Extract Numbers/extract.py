# Extract Numbers from a Document

# ? Task
# Extract all numbers from the contents of an input document. Along with the number, also extract the 'position' of the extracted number. Feel free to define your own response/result format.
# The reference in the result should contain the index of the extract number as well as the number itself

def extract_numbers(sentence: str) -> dict:
    numbers = set(num for num in '0123456789')
    last_start = last_add = -1
    results = {}
    for i in range(len(sentence)):
        if sentence[i] in numbers:
            if last_add + 1 == i:
                results[last_start] = results[last_start] + sentence[i]
                last_add = i
            else:
                results[i] = sentence[i]
                last_start = last_add = i
    return results
