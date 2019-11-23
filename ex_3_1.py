"""
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
hrs = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))
opay = 0
if hrs<= 40 :
    rpay = hrs * rate
else:
    otp = 1.5 * rate
    rpay = 40 * rate
    opay = (hrs - 40) * otp
pay = rpay + opay
print("Pay: "+str(pay))
