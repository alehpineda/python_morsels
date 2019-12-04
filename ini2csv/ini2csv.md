# ini2csv.py

Create a program, ini2csv.py, which accepts an INI-like file and converts it to a CSV-like file.

The input files will look like this (this is an EditorConfig file):

```make
[*.py]
indent_style = space
indent_size = 4

[*.js]
indent_style = space
indent_size = 2
```

Given that input file, .editorconfig, executing our program like this:

```bash
$ python ini2csv.py .editorconfig editorconfig.csv
```

Will produce an output file, editorconfig.csv, like this:

```make
*.py,indent_style,space
*.py,indent_size,4
*.js,indent_style,space
*.js,indent_size,2
```

# Bonus 1

There's just one bonus this week. For the bonus, I'd like you to accept a --collapsed argument that, when present, will collapse the rows to one row per section.

So this:

```bash
$ python ini2csv.py --collapsed .editorconfig editorconfig.csv
```

Will result in a editorconfig.csv file that contains this:

```make
header,indent_style,indent_size
*.py,space,4
*.js,space,2
```
