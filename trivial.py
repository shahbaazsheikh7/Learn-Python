import random
while True:
    ans = input("Enter y to play or done to quit: ")
    if ans == "y":
        dice = random.randrange(1,7)
        print(dice)
    elif ans == "done":
        break
    else:
        print("Please enter valid input.")
        continue

print("GAME OVER")
