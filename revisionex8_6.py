"""Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user
enters “done”. Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum
numbers after the loop completes."""
num = []
while True:
    val = input("Enter a number: ")
    if val == "done":
        break
    try:
        vali = int(val)
    except:
        print("Please enter a number!")
        continue
    num.append(vali)

big = max(num)
small = min(num)
print("The biggest number is %d and the smallest number is %d."%(big,small))
