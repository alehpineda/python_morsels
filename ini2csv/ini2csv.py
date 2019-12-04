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
with open(args.csvfile, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    # if optional argument exist
    if args.collapsed:
        csvwriter.writerow(('header', 'indent_style', 'indent_size'))
        
        for section in config.sections():
            key, value = tuple(config[section].items())
            row = (section, key[1], value[1])
            csvwriter.writerow(row)    
    
    else:
        for section in config.sections():
            for key, value in config[section].items():
                row = (section, key, value)
                csvwriter.writerow(row)            
