# format_fixed_width

Write a function, format_fixed_width, that accepts rows of columns (as a list of lists) and returns a fixed-width formatted string representing the given rows.

For example:

```python
>>> print(format_fixed_width([['green', 'red'], ['blue', 'purple']]))
green  red
blue   purple
```

The padding between the columns should be 2 spaces. Whitespace on the right-hand side of each line should be trimmed and columns should be left-justified.

## Bonus #1

For the first bonus, allow the padding for columns to be specified with an optional padding keyword argument:

```python
>>> rows = [['Robyn', 'Henry', 'Lawrence'], ['John', 'Barbara', 'Gross'], ['Jennifer', '', 'Bixler']]
>>> print(format_fixed_width(rows))
Robyn     Henry    Lawrence
John      Barbara  Gross
Jennifer           Bixler
>>> print(format_fixed_width(rows, padding=1))
Robyn    Henry   Lawrence
John     Barbara Gross
Jennifer          Bixler
>>> print(format_fixed_width(rows, padding=3))
Robyn      Henry     Lawrence
John       Barbara   Gross
Jennifer              Bixler
```

## Bonus #2

For the second bonus, allow column widths to be specified manually with an optional widths keyword argument:

```python
>>> rows = [["Jane", "", "Austen"], ["Samuel", "Langhorne", "Clemens"]]
>>> print(format_fixed_width(rows, widths=[10, 10, 10]))
Jane                    Austen
Samuel      Langhorne   Clemens
```

## Bonus #3

For the third bonus, allow column justifications (left or right) to be specified with with an optional alignments keyword argument. This argument will take lists of 'L' and 'R' strings representing left and right:

```python
>>> print(format_fixed_width(rows, alignments=['R', 'L', 'R']))
  Jane              Austen
Samuel  Langhorne  Clemens
```
