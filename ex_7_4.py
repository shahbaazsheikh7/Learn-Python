fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("Error : Invalid filename.")
    quit()

count = 0
senders = 0
for line in fhand:
    count = count + 1
    if line.startswith("From:"):
        senders = senders + 1

print("This doc contains %d lines"%count)
print("Messages were sent from",senders,"senders.")
