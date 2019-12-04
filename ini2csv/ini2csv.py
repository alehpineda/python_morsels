# add command line arguments
# use argparse
import argparse

# Read ini like file
# use config parser
import configparser

# Read and write csv file
# use csv
import csv

# help flag provides flag help
# store_true actions stores argument as True

parser = argparse.ArgumentParser()

# First argument
parser.add_argument('inifile', help="Load INI-like file")

# Second argument
parser.add_argument('csvfile', help="Destination csv file")

# Third argument and optional
parser.add_argument('--collapsed', action='store_true', help="collapse the rows to one row per section")

# parse the arguments
args = parser.parse_args()

# read and parse the ini-like file
config = configparser.ConfigParser()
config.read(args.inifile)


# Write csvfile
# newline='' needed for windows
with open(args.csvfile, 'w', newline='') as csvfile:

    # if optional argument exist
    if args.collapsed:
        rows = [
            {'header': name, **section}
            for name, section in config.items()
            if section
        ]
        csvwriter = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
        csvwriter.writeheader()
        csvwriter.writerows(rows)
    
    else:
        csvwriter = csv.writer(csvfile)
        # generator comprehension.
        # Use writerows instead of row
        csvwriter.writerows(
            (name, key, value)
            for name, section in config.items()
            for key, value in section.items()
        )           
