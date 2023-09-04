def calculate_pay(hours, rate):
    if (isinstance(hours, str)) or (isinstance(rate, str)):
        print('Error')
        quit()

    hours = float(hours)
    rate = float(rate)

    if hours > 40:
        overtimeHours = hours - 40
        overtimeRate = rate * 1.5

        pay = (40 * rate) + (overtimeHours * overtimeRate)

        return pay
    else:
        pay = hours * rate

        return pay
    
hours = input('Hours:')
rate = input('Rate:')

hoursFloat = float(hours)
rateFloat = float(rate)

pay = calculate_pay(hoursFloat, rateFloat)

print('Pay', pay)
