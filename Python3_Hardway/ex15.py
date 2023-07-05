# Exercise 15: Reading Files
# This exercise involves writing two files. One is the usual ex15.py file
# that you will run and other is named ex15_sample.txt, which is just a plain text file.

from sys import argv

script, filename = argv

txt = open(filename)
print(f"Here's your file {filename}: ")
print(txt.read())

print("Type the filename again: ")
file_again = input("--> ")

txt_again = open(file_again)
print(txt_again.read())

txt.close()