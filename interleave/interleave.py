from more_itertools import roundrobin


def interleave(*iterables):
    """ roundrobin('ABC', 'D', 'EF') --> A D E B F C """
    return roundrobin(*iterables)


def interleave2(*iterables):
    """
        Accepts iterables and return a new iterable with each ot the given
        items interleaved.
    """
    iterators = [iter(i) for i in iterables]
    while iterators:
        for iterator in list(iterators):
            try:
                yield next(iterator)
            except StopIteration:
                iterators.remove(iterator)
