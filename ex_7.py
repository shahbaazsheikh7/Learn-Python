fhand = open("pymbox.txt")
print(fhand)
count = 0

for line in fhand:
    line = line.rstrip()
    if line.find("@uct.ac.za") == -1:
        continue
    print(line)
