# Count the number of words in a text file and also return the 20most used words.
fname = input("Enter the file:")
fhand = open(fname)

counts = {} #initialising empty dictionary.
wordcount = 0 #initialising variable for keeping count of words.
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    for index in range(len(words)):
        counts[words[index]] = counts.get(words[index],0) + 1
        wordcount += 1

tmp = []
for k,v in counts.items():
    tmp.append((v,k))

tmpn = sorted(tmp, reverse = True)
print("The number of words in the book: ",wordcount,"words")
print("The 20 most used words are:")
for k,v in tmpn[:20]:
    print(v,":",k,"times.")
