# Exercise 2: Write a program to prompt for a file name, and then read through the
# file and look for lines of the form:
# X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
# the line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

fname = input("Enter a file name: ")
fhand = open(fname)
count = 0
sum = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        zpos = line.find("0")
        xstr = line[zpos:]
        flt = float(xstr)
        sum = sum + flt
print("Average spam confidence:",sum/count)
