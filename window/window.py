from itertools import islice, tee
from typing import Iterable


def window(iterable: Iterable, number: int, *, fillvalue=None) -> Iterable:
    iters = tee(iterable, number)
    for i, it in enumerate(iters):
        next(islice(it, i, i), fillvalue)
    return zip(*iters)


if __name__ == "__main__":
    print(len(list(window([], 1))))
    print(len(list(window([1, 2], 3))))
    print(len(list(window([1, 2, 3], 4))))
    print(len(list(window([1, 2, 3, 4], 5))))
