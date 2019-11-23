#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line check to see if the word is already in the list
#and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
fname = input("Enter the filename:  ")
fhand = open(fname)
t = list()  #initialising the empty list
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for index in range(len(words)):
        if words[index] in t:
            continue
        t.append(words[index])

t.sort()
print(t)
