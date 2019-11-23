import re

fname = input("Enter file: ")
fhand = open(fname)

lst = []
for line in fhand:
    x = re.findall('[0-9]+',line)
    for i in range(len(x)):
        x[i] = int(x[i])
    lst.extend(x)

print("Sum:",sum(lst))
