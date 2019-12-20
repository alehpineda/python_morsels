from itertools import groupby


def compact1(iterable):
    """
    This works only for lists
    """
    if len(iterable) < 2:
        return iterable

    return [iterable[e] for e in range(len(iterable))
            if e == 0 or iterable[e] != iterable[e - 1]]


def compact2(iterable):
    """
    This works for iterables
    and returns a list
    """
    return [k for k, _ in groupby(iterable)]


def compact(iterable):
    """
    This works for iterables
    and return an iterable
    """
    return (key for key, _ in groupby(iterable))
