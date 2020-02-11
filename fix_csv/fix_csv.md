# fix_csv.py

We're going to normalize CSV files by writing a program, fix_csv.py,
that turns a pipe-delimited file into a comma-delimited file. I'll
explain how it should work by example.

Your original file will look like this:

Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
You'll then run your script by typing this at the command line:

$ python fix_csv.py cars-original.csv cars.csv
Note : "$" is not typed; that is simply the beginning of the prompt.

Your fixed file should then look like this:

Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257

- Bonus 1

For the first bonus, I want you to allow the input delimiter and quote
character to be optionally specified. ✔️

For example any of these should work (all specify input delimiter as
pipe and the last two additionally specifies the quote character as
single quote):

$ python fix_csv.py --in-delimiter="|" cars.csv cars-fixed.csv
$ python fix_csv.py cars.csv cars-fixed.csv --in-delimiter="|"
$ python fix_csv.py --in-delimiter="|" --in-quote="'" cars.csv cars-fixed.csv
$ python fix_csv.py --in-quote="'" --in-delimiter="|" cars.csv cars-fixed.csv
This bonus will require looking into parsing command-line arguments with 
Python. There are some standard library modules that can help you out 
with this. There are 3 different solutions in the standard library 
actually, but only one I'd recommend.

- Bonus 2

For the second bonus, automatically detect the delimiter if an 
in-delimiter value isn't supplied (don't assume it's pipe and quote, 
figure it out). ✔️

This second bonus is a bit trickier and I don't expect it to work 
correctly for all files. You'll likely want to consult the csv module 
documentation if you're going to attempt it.
"""