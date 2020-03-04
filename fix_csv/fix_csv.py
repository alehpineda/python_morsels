import argparse
import csv

# Parser
parser = argparse.ArgumentParser(description='Normalize CSV files')
parser.add_argument('original_file', type=str, help='Specify original file')
parser.add_argument('fixed_file', type=str, help='Specify fixed file')
parser.add_argument('--in-delimiter', type=str, help='Specify input delimiter')
parser.add_argument('--in-quote', type=str, help='specify input quote')

args = parser.parse_args()

# read csv
with open(args.original_file, newline='') as original_file:
    if args.in_delimiter and args.in_quote:
        rows = list(csv.reader(original_file,
                               delimiter=args.in_delimiter,
                               quotechar=args.in_quote))
    else:
        dialect = csv.Sniffer().sniff(original_file.read())
        original_file.seek(0)
        rows = list(csv.reader(original_file, dialect=dialect))

# write csv
with open(args.fixed_file, mode='wt', newline='') as fix_file:
    csv.writer(fix_file).writerows(rows)
