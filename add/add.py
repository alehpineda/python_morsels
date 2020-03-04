from typing import List
from itertools import zip_longest


def add(*args: List) -> List:
    try:
        return [list(map(sum, zip_longest(*t))) for t in zip_longest(*args)]
    except TypeError:
        raise ValueError
