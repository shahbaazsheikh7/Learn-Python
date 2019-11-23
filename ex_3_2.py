"""
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
"""
hrs = input("Enter Hours: ")
try:
    hrf = int(hrs)
except:
    print("Error, please enter a numeric value!")
    quit()

rts = input("Enter Rate: ")
try:
    rtf = float(rts)
except:
    print("Error, please enter a numeric value!")
    quit()

if hrf>40 :
    opay = (hrf - 40) * rtf * 1.5
    rpay = 40 * rtf
    pay = opay + rpay
else:
    pay = hrf * rtf

print("Pay: ",pay)
