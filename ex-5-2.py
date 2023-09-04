# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below. 

largest = None
smallest = None

while True:
    userInput = input('Enter a number: ')

    try:
        inputFloat = float(userInput)

        if largest is None:
            largest = inputFloat
        else:
            if inputFloat > largest:
                largest = inputFloat

        if smallest is None:
            smallest = inputFloat
        else:
            if inputFloat < smallest:
                smallest = inputFloat

    except Exception as e:
        if userInput.lower() != 'done':
            print('Invalid input')
        else:
            break

print('Maximum is', largest / 1)
print('Minimum is', smallest / 1)
