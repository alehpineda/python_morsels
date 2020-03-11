from io import StringIO
from itertools import groupby
from operator import itemgetter
import csv


def condense_csv(csv_text, id_name=None):
    groups = []
    csv_reader = csv.reader(csv_text.splitlines())

    if id_name is None:
        [id_name, *other_headers] = next(csv_reader)

    attrs = [id_name]

    for _id, _rows in groupby(csv_reader, key=itemgetter(0)):
        group = {_attr: _value for _id, _attr, _value in _rows}
        group[id_name] = _id
        groups.append(group)
        attrs.extend(group.keys())

    out_file = StringIO()
    headers = dict.fromkeys(attrs, None).keys()
    writer = csv.DictWriter(out_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(groups)

    return out_file.getvalue()
