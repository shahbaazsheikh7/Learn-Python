"""Write a program that categorizes each mail message by which day of
the week the commit was done. To do this look for lines that start with “From”,
then look for the third word and keep a running count of each of the days of the
week. At the end of the program print out the contents of your dictionary (order
does not matter)."""
fname = input("Enter the filename: ")
fhand = open(fname)
counts = {}
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0]!="From":
        continue
    for index in words:
        counts[words[2]] = counts.get(words[2],0) + 1

print(counts)
