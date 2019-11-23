#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear
#in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the
#most prolific committer.
fname = input("Enter the filename: ")
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words)==0 or words[0] != "From":
        continue
    counts[words[1]] = counts.get(words[1],0) + 1

send = None
count = None
for mail,rep in counts.items():
    if count is None or rep > count:
        send = mail
        count = rep

print(send,count)
