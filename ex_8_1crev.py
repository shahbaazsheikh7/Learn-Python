"""Write a function called chop that takes a list and modifies it, removing the first
and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list that
contains all but the first and last elements.
"""
def chop(t):
    del(t[0])
    del(t[-1])

def middle(lst):
    return lst[1:len(lst)-1]

inp = input("Enter the list elements(with spaces between the elements): ")
delimiter = " "
lst = inp.split(delimiter)
chop(lst)
print(lst)

inpagn = input("Enter the list elements(with spaces between the elements): ")
delimiter = " "
nlst = inpagn.split(delimiter)
mlst = middle(nlst)
print(mlst)
print(nlst) 
