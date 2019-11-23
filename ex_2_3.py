#Exercise 3: Write a program to prompt the user for hours and rate per
#hour to compute gross pay.
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25

hours = int(input("Enter hours: "))
rate = float(input("Enter Rate: "))
pay = hours * rate
print("Pay: ",pay)
