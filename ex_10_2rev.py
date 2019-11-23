#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fname = input("Enter a filename: ")
try:
    fhand = open(fname)
except:
    print("Invalid input")
    exit()
hours = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0]!="From":
        continue
    hr = words[5]
    hrs = hr.split(":")
    hours[hrs[0]] = hours.get(hrs[0],0) + 1

lst = sorted(hours.items())

for k,v in lst:
    print(k,v)
