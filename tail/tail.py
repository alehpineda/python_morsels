from collections import deque

def tail(sequence, number):
    """
    function that takes a sequence (like a list, string, or tuple) 
    and a number n and returns the last n elements from the given 
    sequence, as a list.
    """
    if number < 1:
        return []
    
    d = deque(maxlen=number)
    d.extend(sequence)
    
    return list(d)

# Python morsels solution

def tail1(iterable, n):
    """Return the last n items of given iterable."""
    if n <= 0:
        return []
    return list(deque(iterable, maxlen=n))
