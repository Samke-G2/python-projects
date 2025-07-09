# Exercise 17 - More Files

# It seems I've commented most of the code out, but it still works...how??
# Well, one of the study drills is to see how short i can make the script. Zed's limit is 1 line...my best is 2 lines.

# New terminal commands learned:
#   echo <some text as string> > <the name of new file.txt> -   creates a new text file on the fly
#   cat <name of file> reads the file (displaying it) on hte terminal

from sys import argv; from os.path import exists; script, from_file, to_file = argv; indata = open(from_file).read(); out_file = open(to_file, "w").write(indata)

# print(f"Copying from {from_file} to {to_file}")

# we could do these two in one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# This is the one-line way of doing line 11 and 12
# indata = open(from_file).read()

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print(f"Ready, hit ENTER to continue, CTRL -C to abort.")
# input("?")

# This li
# input("Ready, hit ENTER to continue, CTRL -C to abort. ")

# out_file = open(to_file, "w").write(indata)
# out_file.write(indata)

# print("...")
# print("Alright, all done.")

# out_file.close()
# from_file.close()                 - The one-line method of opening and reading th file used in hte second draft does not need hte closing statement.
