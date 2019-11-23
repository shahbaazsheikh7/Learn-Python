"""Write a program to read through a mail log, build a histogram using
a dictionary to count how many messages have come from each email address, and
print the dictionary."""
fname = input("Enter the filename: ")
fhand = open(fname)
mails_count = {}
big = None
bigmail = None
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != "From":
        continue
    for index in range(len(words)):
        mails_count[words[1]] = mails_count.get(words[1],0) + 1
        if big is None or mails_count[words[1]] > big:
            big = mails_count[words[1]]

print(big,mails_count[big])
