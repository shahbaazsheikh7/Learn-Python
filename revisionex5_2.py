"""Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average."""

max = None
min = None

while True:
    num = input("Enter the number: ")
    if(num == "done"):
        break
    try:
        numi = int(num)
    except:
        print("Invalid input")
        continue

    if max is None or max < numi:
        max = numi

    if min is None or min > numi:
        min = numi

print("Max:",max,"Min:",min)
