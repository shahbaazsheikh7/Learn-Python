largest = None
smallest = None
while True:
    nums = input("Enter a number: ")
    if nums == "done":
        break
    try:
        numi = int(nums)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = numi
    if smallest is None:
        smallest = numi
    if numi > largest:
        largest = numi
    if numi < smallest:
        smallest = numi

print("Maximum is",largest)
print("Minimum is",smallest)
