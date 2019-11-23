"""Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number."""

sum = 0
count = 0

while True:
    num = input("Enter a number: ")
    if(num=="done"):
        break
    try:
        numi = int(num)
    except:
        print("Invalid input")
        continue

    count += 1
    sum = sum + numi

#print the total, count and average
print(sum,count,sum/count)
