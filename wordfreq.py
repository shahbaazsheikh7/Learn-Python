# Program to compute most used words in a text file
import string                       #importing the string module
import matplotlib.pyplot as plt    #importing the matplotlib module for plotting

fname = input("Enter the filname: ") # taking the input of filename from the user

try:
    fhand = open(fname)  # try opening the file
except:
    print("Invalid filename")   #if it fails, then print this and exit
    exit()

wordcount = {}  #intialize empty dictionary
cnt = 0        #set the count to zero

for line in fhand:     #looping through the file, line by line
    line = line.translate(str.maketrans('','',string.punctuation)) #removing punctuation marks
    line = line.strip()  #remove whitespace
    line = line.lower()   #make all the words lowercase
    words = line.split()  #make a list of all the words
    if len(words)==0:
        continue         # if the length of the list is zero(if we encounter a blank line in a file), then continue to the next line
    for word in words:     # loop through the items in the list
        wordcount[word] = wordcount.get(word,0) + 1  # dictionary .get method to count the occurence of word
        cnt = cnt + 1                  #cnt is for counnting the number of words in the file
        #print(count)

wordlist = []
#print(type(wordcount.items()))
for word,count in wordcount.items():
    wordlist.append((count,word))   #wordlist is list of tuples-- (count,word)
#print(type(wordlist[0]))
wordlist.sort(reverse=True)

print(fname,"contains",cnt,"words")
print("The 10 most used words in %s are: "%fname)

count_list = []
word_list = []

for count,word in wordlist[:10]:
    print(word,count)
    word_list.append(word)
    count_list.append(count)

plt.xlabel("Words",color="Green")
plt.ylabel("Number of Occurences",color="Green")
plt.title("Top 10 most used words in '%s'"%fname,color="Green")
#plt.legend("'%s' has %d words"%(fname,cnt))
plt.bar(word_list,count_list)
plt.show()
