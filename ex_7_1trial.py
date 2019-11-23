""" Write a program to read through a file and print the contents of the
file (line by line) all in upper case. """

fname = input("Enter a filename: ")
try:
    fhand = open(fname)
except:
    print("Invalid filename")
    quit()
for line in fhand:
    line = line.strip()
    line = line.upper()
    print(line)
