from collections.abc import MutableSet, Sequence


class OrderedSet(MutableSet):
    def __init__(self, items):
        self.items = dict.fromkeys(items, None)

    def __iter__(self):
        for item in self.items:
            yield item

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    # Bonus 1 - add and discard
    def add(self, item):
        self.items[item] = None

    def discard(self, item):
        self.items.pop(item, None)

    # Bonus 2 - Equality
    def __eq__(self, other):
        if not isinstance(other, OrderedSet):
            return self.items.keys() == other

        return tuple(self.items.keys()) == tuple(other.items.keys())

    # Bonus 3 - Supports index
    def __getitem__(self, i):
        return list(self.items.items())[i][0]


class OrderedSet2(Sequence, MutableSet):

    """Set-like object that maintains insertion order of items."""

    def __init__(self, iterable):
        self.items = set()
        self.order = []
        self |= iterable

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.order[index]

    def add(self, item):
        if item not in self.items:
            self.order.append(item)
        self.items.add(item)

    def discard(self, item):
        if item in self.items:
            self.order.remove(item)
            self.items.remove(item)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return len(self) == len(other) and all(
                x == y for x, y in zip(self, other)
            )
        return super().__eq__(other)
