import sys
name = input("Enter your name: ")
ages = input("Enter your age: ")
agei = int(ages)
print(name, "you'll be 100 years old in",(2018+(100-agei)))
print("type exit to exit:")
resp=input()
if resp=="exit":
    sys.exit()
