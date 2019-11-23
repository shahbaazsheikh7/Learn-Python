"""Write a program that reads a file and prints the letters in decreasing
order of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits, punctuation,
or anything other than the letters a-z. Find text samples from several different
languages and see how letter frequency varies between languages. Compare your
results with the tables at wikipedia.org/wiki/Letter_frequencies."""
import string
import matplotlib.pyplot as plt

fname = input("Enter the filname: ")

try:
    fhand = open(fname)
except:
    print("Invalid filename")
    exit()

lfq = {}         #intialize letter frequency dictionary

for line in fhand:                              #parse through each line of the file
    line = line.translate(str.maketrans('','',string.punctuation)) #get rid of punctuation marks using the translate method
    line = line.lower()                     #convert all string to lowercase
    words = line.split()                   #create a list of words using the split method
    if len(words) == 0 :
        continue
    for word in words:                   #loop through each word in the words list
        letters = str(word)             #convert each word in the list to string
        for var in letters:                 #loop through each character in the word
            if var >= "a" and var<="z":            #if the character is an alphabet, add it to the dictionary
                lfq[var] = lfq.get(var,0) + 1         #adding to the dictionary using the GET method
            else:
                continue                         #skip uninteresting characters

letterlist = sorted(lfq.items())          #create a sorted list (of tuples) by calling SORTED function on dictionary.items()
#which returns a list of tuples(key,value)
letter_list = []
freq_list = []

for letter,freq in letterlist:                  #loop through the sorted list (letter, freq is the tuple assignment, Since each element of the list is a tuple)
    print(letter,freq)
    letter_list.append(letter)
    freq_list.append(freq)
#print(len(letter_list))
#print(len(freq_list))

plt.xlabel("Letters",color="Green")
plt.ylabel("Frequency",color="Green")
plt.title("Letter Frequency distribution in '%s'"%fname,color="Green")

plt.bar(letter_list,freq_list)
plt.show()
