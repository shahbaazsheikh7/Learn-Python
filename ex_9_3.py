"""Write a program to read through a mail log, build a histogram using
a dictionary to count how many messages have come from each email address, and
print the dictionary."""
fname = input("Enter the filename: ")
try:
    fhand = open(fname)
except:
    print("invalid filename")
    exit()
mails = {}
for line in fhand:
    words = line.split()
    if len(words)==0 or words[0]!="From":
        continue
    mails[words[1]] = mails.get(words[1],0) + 1
print(mails)
