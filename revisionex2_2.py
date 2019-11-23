def computepay(hrs,rate):

    try:
        hri = int(hrs)
    except:
        print("Enter numeric input!")
        quit()


    try:
        rt = float(rate)
    except:
        print("Enter numeric input!")
        quit()

    rpay = hri * rt
    opay = (hri - 40) * (0.5) * rt

    if hri>40:
        pay = rpay + opay
    else:
        pay = rpay
    return pay

hrs = input("Enter the hours: ")
rate = input("Enter the hourly rate: ")
pay = computepay(hrs,rate)
print("Pay:",pay)
