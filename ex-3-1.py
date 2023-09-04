hrs = input("Enter Hours:")
rate = input('Enter Rate:')
h = float(hrs)
r = float(rate)

if h <= 40 :
    regPay = h * r;
    print(regPay)
else :
    hrsOverForty = h - 40
    overtimeRate = r * 1.5
    regPay = h * r
    overPay = hrsOverForty * overtimeRate
    print(regPay + overPay)
