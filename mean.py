nums = input("Enter the number till which you want to calculate mean: ")
numi = int(nums)
count = 0
sum = 0
i = 1
while i<=numi:
    count = count + 1
    sum = sum + i
    i = i + 1
print("The mean of natural numbers till",numi,"is",sum/count)
