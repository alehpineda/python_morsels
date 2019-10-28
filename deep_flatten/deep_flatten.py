from collections.abc import Iterable

# Write a function that returns a flattened version of that list.

def deep_flatten(lst):
    for element in lst:
        if isinstance(element, str):
            yield element
             
        elif isinstance(element, Iterable):
            yield from deep_flatten(element)

        else:
            yield element
