def chop(t):
    del(t[0])
    del(t[-1])

t = input("Enter the list elements(with space between the elements):  ")
delimiter = " "
tn = t.split(delimiter)
chop(tn)
print(tn)
