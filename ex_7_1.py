fname = input("Enter a fiename: ")
try:
    fhand = open(fname)
except:
    print("Error: Please enter correct filename.")
    quit()
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)
