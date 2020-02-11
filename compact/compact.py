from itertools import groupby


def compact(iterable):
    """
    This works for iterables
    and return an iterable
    """
    return (key for key, _ in groupby(iterable))
