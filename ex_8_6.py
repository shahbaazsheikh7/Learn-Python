smallest = None
largest = None
num = list()
index = 0
while True:
    inp = input("Enter a number:  ")
    try:
        numi = int(inp)
    except:
        if inp=="done":
            break
        print("Please enter a number")
        continue
    if numi in num:
        continue
    num.append(numi)
    if smallest is None:
        smallest = num[index]
    if largest is None:
        largest = num[index]
    if smallest > num[index]:
        smallest = num[index]
    if largest < num[index]:
        largest = num[index]
    index += 1

print("Maximum:",largest)
print("Minimum:",smallest)
