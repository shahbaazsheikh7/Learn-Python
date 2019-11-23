def computegrade(scores):
    try:
        scorei = float(scores)
    except:
        return("Bad Score")
    if scorei<=1.0 and scorei>=0.0:
        if scorei>=0.9:
            grade = "A"
        elif scorei>=0.8:
            grade = "B"
        elif scorei>=0.7:
            grade = "C"
        elif scorei>=0.6:
            grade = "D"
        else:
            grade = "F"
    else:
        return("Bad Score")

    return grade

sc = input("Enter score: ")
fs = computegrade(sc)
print(fs)
