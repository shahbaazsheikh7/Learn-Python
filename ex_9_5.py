"""This program records the domain name (instead of the address) where
the message was sent from instead of who the mail came from (i.e., the whole email
address). At the end of the program, print out the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""
fname = input("Enter the filename: ")
domains = []
counts = {}
try:
    fhand = open(fname)
except:
    print("Invalid input")
    exit()
for line in fhand:
    words = line.split()
    if len(words)==0 or words[0]!="From":
        continue
    addr = str(words[1])
    atpos = addr.find("@")
    domain = addr[atpos+1:]
    domains.append(domain)

for var in domains:
    counts[var] = counts.get(var,0) + 1

print(counts)
