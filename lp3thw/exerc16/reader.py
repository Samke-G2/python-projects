# script to read the sample file

from sys import argv

script, filename = argv

file = open(filename, "r")

print(file.read())
