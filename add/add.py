from typing import List
from itertools import zip_longest

def add(*args: list) -> list:
    # for t in zip(m1, m2)
    # t returns a zip of each row of m1 and m2
    # map(sum, zip(*t))
    # map sums each the unzip rows
    # list() converts de map objects
    # [] list comprehension
    # Bonus 1 -> sum all the matrices!
    # change *args
    # extract all the args
    # Bonus 2 -> Raise value error if matrices not equal
    # all(len(i) == len(x[0]) for i in x)
    # for each list in args check all the len of the list against
    # the len of the first args.
    #if all(all(len(i) == len(x[0]) for i in x) and len(x) == len(args[0]) for x in args):
    
    try:
        return [list(map(sum, zip_longest(*t))) for t in zip_longest(*args)]
    except TypeError:
        raise ValueError
