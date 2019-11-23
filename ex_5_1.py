sum = 0
count = 0
while True:
    nums = input("Enter the number: ")
    if nums == "done":
        break
    try:
        numi = float(nums)
    except:
        print("Invalid input")
        continue
    sum = sum + nums
    count = count + 1

print(sum,count,sum/count)
