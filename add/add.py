""" add function """
from typing import List
from itertools import zip_longest


def add(*args: List) -> List:
    """
        Function that accepts two lists-of-lists of numbers and returns one
        list-of-lists with each of the corresponding numbers in the two given
        lists-of-lists added together.
    """
    try:
        return [list(map(sum, zip_longest(*t))) for t in zip_longest(*args)]
    except TypeError:
        raise ValueError
