from collections import defaultdict


def condense_csv(csv_text, id_name):
    groups = defaultdict(dict)
    for row in csv_text.splitlines():
        _id, _attr, _value = row.split(',')
        groups[_id][_attr] = _value

    headers = [id_name, *groups[_id].keys()]
    rows = [[_id, *_attr.values()] for _id, _attr in groups.items()]
    return '\n'.join(','.join(row) for row in [headers, *rows])
