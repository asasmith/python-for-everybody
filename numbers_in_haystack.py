import re

fileHandle = open('actual_data.txt')

accumulator = []

for line in fileHandle:
    numbers = re.findall('[0-9]+', line)
    if numbers:
        for num in numbers:
            accumulator.append(int(num))

print(sum(accumulator))
