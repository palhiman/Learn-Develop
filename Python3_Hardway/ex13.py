# Parameters, Unpacking and Variables

from sys import argv # argv is called "Argument variables".
# read the WYSS section for how to run this
script, first, second, third = argv # this is called unpacking of arguments to variables.

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)