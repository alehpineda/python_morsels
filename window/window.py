from collections import deque
from typing import Iterable


def window(iterable: Iterable, number: int, *, fillvalue=None) -> Iterable:
    if number == 0:
        return
    iterator = iter(iterable)
    current = deque(maxlen=number)
    for _ in range(number):
        current.append(next(iterator, fillvalue))
    yield tuple(current)
    for item in iterator:
        current.append(item)
        yield tuple(current)
