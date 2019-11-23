fname = input("Enter the filename: ")
fhand = open(fname)

counts = {}
wordcount = 0
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

print("The book has",wordcount,"words.")
print("The 20 most used words are: ")
for k,v in tmpn[:20]:
    print(v,":",k,"times.") 
