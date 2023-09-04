# Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

isRunning = True
total = 0
count = 0
average = 0

while isRunning:
    inputVal = input('Enter a number: ');

    try:
        inputValFloat = float(inputVal)
    except Exception as e:
        if inputVal.lower() == 'done':
            break
        else:
            print('not a valid number')

    total = total + inputValFloat
    count = count + 1


print('Total: ', total)
print('Count: ', count)
print('Avg: ', total / count)
