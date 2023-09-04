# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

file = input('Enter file name: ')

lineCount = 0
xDspamConfidenceTotal = 0

try:
    fileHandle = open(file)

except:
    print('Filename was invalid')
    quit();

for line in fileHandle:
    if line.startswith('X-DSPAM-Confidence:'):
        colonPos = line.find(':')
        subStr = line[colonPos + 1:]
        subStrFloat = float(subStr)
        lineCount = lineCount + 1
        xDspamConfidenceTotal = xDspamConfidenceTotal + subStrFloat
        
print('Average spam confidence:',xDspamConfidenceTotal / lineCount)

