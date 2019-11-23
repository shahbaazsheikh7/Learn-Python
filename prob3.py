"""Find largest prime factor of a given number: """

prime = []
num = int(input("Enter the number: "))
for i in range(num//2):
    if num%i!=0:
        continue
    else:
        for x in range(i):
            if i%x==0:
                continue
            else:
                prime.append(i)
print(prime)
