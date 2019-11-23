"""Revise a previous program as follows: Read and parse the “From”
lines and pull out the addresses from the line. Count the number of messages from
each person using a dictionary.
After all the data has been read, print the person with the most commits by
creating a list of (count, email) tuples from the dictionary. Then sort the list in
reverse order and print out the person who has the most commits."""
import string
fname = input("Enter a filename: ")
try:
    fhand = open(fname)
except:
    print("Invalid filename")
    exit()
counts = {}
for line in fhand:
    words = line.split()
    if len(words)==0 or words[0]!="From":
        continue
    counts[words[1]] = counts.get(words[1],0) + 1

mails = []
for key,value in counts.items():
    mails.append((value,key))

mails.sort(reverse=True)

print(mails[0])
