from itertools import groupby, count
from collections import Counter

def format_ranges(list_numbers):
    num_groups = []
    counter = count()

    #print(*_unique_ranges(list_numbers))

    for unique_range in _unique_ranges(list_numbers):
        #print(unique_range)
        for _, group in groupby(sorted(unique_range), lambda x:x-next(counter)):
            group = list(group)
            #print(f'lista: {sorted(list_numbers)}')
            #print(f'group: {group}')
            #print(f'diff: {[x for x in sorted(list_numbers) if x not in set(group)]}')
            if len(group) > 1:
                #print(f'TRUE: {group[0]}-{group[-1]}')
                num_groups.append(f'{group[0]}-{group[-1]}')
            
            else:
                #print(f'FALSE: {group[0]}')
                num_groups.append(f'{group[0]}')
    
    #print(num_groups)
    #print(sorted(num_groups))

    return ','.join(num_groups)

def _unique_ranges(list_numbers):
    count = Counter(list_numbers)
    #sets = []
    #print(list(set(count.elements())), len(set(count.elements())))
    while len(set(count.elements())) > 0:
        #print(list(set(count.elements())))
        yield list(set(count.elements()))
        #sets.append(list(set(count.elements()) ) )
        count.subtract(set(count.elements()))
    
    #return order_sets(sets)

def order_sets(set):
    # order the set by the minimun value of the set and
    # the minimum len
    pass
