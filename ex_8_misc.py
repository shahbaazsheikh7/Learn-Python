""" write a program to read the file mbox-short.txt and print the days from the mails."""
fname = input("Enter the filename: ")
fhand = open(fname)
for line in fhand:
    words = line.split()
    if len(words)==0:
        continue
    if words[0]!="From":
        continue
    print(words[2])
