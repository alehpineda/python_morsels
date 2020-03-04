import re


# definind funtion parse_ranges
def parse_ranges(lists):
    # For each element in list split by ','
    for element in lists.split(','):
        # unpack the variables by the partition in '-'
        start, found, end = element.partition('-')
        # match re pattern
        match = re.search(r'(->.+)', element)
        # if found exists and not match
        if found and not match:
            # yield the range from the generator
            yield from (x for x in range(int(start), int(end)+1))
        # else if match exists
        elif match:
            # yield the start only
            yield int(start)
        else:
            # Else yield the element
            yield int(element)
