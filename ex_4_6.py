def computepay(h,r):
    if h>40:
        reg = h * r
        otp = (h-40) * (0.5 * r)
        pay = reg + otp
    else:
        pay = h * r
    return pay

hrs = input("Enter Hours:")
try:
    hrf = float(hrs)
except:
    print("Error: Please enter numeric value.")
    quit()
rs = input("Enter hourly rate:")
try:
    rf = float(rs)
except:
    print("Error: Please enter numeric value.")

fpay = computepay(hrf,rf)
print(fpay)
