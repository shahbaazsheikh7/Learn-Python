def middle(t):
    return t[1:len(t)-1]

inp = input("Enter the list(with space between the elements):  ")
delimiter = " "
tn = inp.split(delimiter)
tl = middle(tn)
print(tl)
