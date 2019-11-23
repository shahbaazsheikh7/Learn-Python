"""Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both
the maximum and minimum of the numbers instead of the average."""
count = 0 ; total = 0 ; smallest = None ; biggest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numi = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None or smallest > numi:
        smallest = numi
    if biggest is None or biggest < numi:
        biggest = numi
    count = count + 1
    total = total + numi
print("total:",total," count:", count, " smallest:",smallest," biggest:", biggest)
