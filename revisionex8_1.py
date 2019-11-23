"""Write a function called chop that takes a list and modifies it, removing the first
and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list that
contains all but the first and last elements."""
t = []
while True:
    val = input("Enter a value: ")

    if val == "done":
        break
    t.append(val)

print("The list is",t)

def chop(t):
    del t[0]
    del t[-1]

def middle(t):
    return t[1:len(t)-1]

chop(t)
print(t)

#t1 = middle(t)
#print(t1)
#print(t)
