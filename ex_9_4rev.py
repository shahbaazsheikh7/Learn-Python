"""Add code to the above program to figure out who has the most
messages in the file.
After all the data has been read and the dictionary has been created, look through
the dictionary using a maximum loop (see Section [maximumloop]) to find who
has the most messages and print how many messages the person has."""

fname = input("Enter the filename: ")  #ask for the flie
mails = {}                         #initialize the mails dictionary
try:
    fhand = open(fname)
except:
    print("invalid filename")
    exit()
for line in fhand:                      #parse through the file line by line
    words = line.split()                #use the split method to create a list of words in the line
    if len(words)==0 or words[0]!="From":   #skip uninteresting lines
        continue
    mails[words[1]] = mails.get(words[1],0) + 1     #create a histogram using dictionary and the GET method of dictionary
mail_keys = list(mails.keys())
print(mail_keys)           #create a list of keys(mail ids) using the keys() method of dictionary
mail_keys.sort(reverse=True)                    #sort the keys in reverse order
print(mail_keys[0],mails[mail_keys[0]])
