fname = input("Enter the filename: ")
fout = open("mails.txt","w")
count = 0
try:
    fhand = open(fname)
except:
    print("Enter valid filename")
    quit()
for line in fhand:
    if not line.startswith("From:"):
        continue
    fout.write(line)
    count = count + 1
fout.write("There are "+str(count)+" mails.")
fout.close()
