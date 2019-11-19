from itertools import groupby, count
from collections import Counter

def format_ranges(list_numbers):
    num_groups = []
    counter = count()

    for unique_range in _unique_ranges(list_numbers):

        for _, group in groupby(sorted(unique_range), lambda x:x-next(counter)):
            group = list(group)

            if len(group) > 1:
                num_groups.append((group[0], group[-1]))
            
            else:
                num_groups.append((group[0],))

    range_groups = (f'{r[0]}-{r[-1]}' if len(r) > 1 else f'{r[0]}' for r in sorted(num_groups))

    return ','.join(range_groups)

def _unique_ranges(list_numbers):
    count = Counter(list_numbers)

    while len(set(count.elements())) > 0:
        yield list(set(count.elements()))
        count.subtract(set(count.elements()))
