from collections.abc import Iterable

# Write a function that returns a flattened version of that list.

def deep_flatten(lst):
    # For each element in the list
    for element in lst:
        # If the element is instance of Iterable and not instance of string
        if isinstance(element, Iterable) and not isinstance(element, str):
            # Yield the element recursively from deep_flatten 
            yield from deep_flatten(element)

        else:
            # Else yield the element
            yield element
