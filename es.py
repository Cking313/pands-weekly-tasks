# es.py
# Prints the number of es in a file
# Author: Colleen King
# need sys to get the command line arguments
# https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments
import sys
import pathlib

# https://docs.python.org/3/tutorial/errors.html
try:
    # make sure there's at least one command line argument (argv[0] is the program name)
    filename = sys.argv[1]
# if we get an indexerror, the list doesn't have an element 1, so there's no filename
except IndexError:
    print('No filename supplied')
    raise

# check if the filename is a file using pathlib
# https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/
file = pathlib.Path(filename)
if not file.is_file():
    raise ValueError("Provided filepath does not exist")

# https://www.w3schools.com/python/python_file_open.asp
# open the path in r (read) mode, store the text in a variable, and count the es
with open(file, 'r') as f:
    data = f.read()
    es = data.count('e')

print(es)