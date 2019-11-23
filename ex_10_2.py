#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fname = input("Enter the filename: ")
fhand = open(fname)

counts = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0]!="From":
        continue
    hour = words[5]
    hr = hour.split(":")
    counts[hr[0]] = counts.get(hr[0],0) + 1

lst = sorted(counts.items())

for k,v in lst:
    print(k,v)
