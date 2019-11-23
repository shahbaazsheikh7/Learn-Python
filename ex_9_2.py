"""Write a program that categorizes each mail message by which day of
the week the commit was done. To do this look for lines that start with “From”,
then look for the third word and keep a running count of each of the days of the
week. At the end of the program print out the contents of your dictionary (order
does not matter).
"""
fname = input("Enter the filename: ")
try:
    fhand = open(fname)
except:
    print("Invalid input")
    exit()
days = {} #initialize the dictionary
for line in fhand:    # parse through the file line by line
    words = line.split()    #make a list of words in a line by the split method
    if len(words)==0 or words[0]!="From": #ignore the uninteresting lines
        continue
    days[words[2]] = days.get(words[2],0) + 1 #add to dictionary by the GET method
#keys = list(days.keys())
#keys.sort()
#for key in keys:
#    print(key,days[key])
print(days)
