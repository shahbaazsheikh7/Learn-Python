"""Write a program to open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is not in
the list, add it to the list.
When the program completes, sort and print the resulting words in alphabetical
order."""
word = []
fname = input("Enter the file: ")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for i in range(len(words)):
        if words[i] in word:
            continue
        else:
            word.append(words[i])

word.sort()
print(word)
