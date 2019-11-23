fname = input("Enter the filename: ")
count = 0

try:
    fhand = open(fname)
    for line in fhand:
        if not line.startswith("From:"):
            continue
        count = count + 1
    print("There are",count, "subject lines in",fname)

except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been Punk'd!")
    else:
        print("File cannot be opened:",fname)
        quit()
