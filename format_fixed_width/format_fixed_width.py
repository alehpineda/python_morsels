def format_fixed_width(matrix, padding=2, widths=[], alignments=[]):
    longest_str = [
        len(max((matrix[i][index] for i, rows in enumerate(matrix)), key=len))
        for _, rows in enumerate(matrix)
        for index, _ in enumerate(rows)
    ]

    fixed = []
    for index, rows in enumerate(matrix):
        sub = []
        for i, elem in enumerate(rows):
            if len(widths) > 0:
                blank = (widths[i] - len(elem)) * " "
            else:
                blank = (longest_str[i] - len(elem)) * " "
            elem += blank + padding * " "
            if i == len(rows) - 1:
                elem = elem.rstrip()
                if index != len(matrix) - 1:
                    elem = elem + "\n"
            sub.append(elem)
        fixed.append(sub)
    return "".join(e for lol in fixed for e in lol)


if __name__ == "__main__":
    rows = [["Samuel", "Langhorne", "Clemens"], ["", "Charlotte", "Brontë"]]
    print(format_fixed_width(rows, widths=[10, 10, 10]))
