# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fileHandle = open('mbox-short.txt')

sentHours = dict()

for line in fileHandle:
    if line.startswith('From '):
        splitLine = line.split()
        timeSplit = splitLine[5].split(':')

        sentHours[timeSplit[0]] = sentHours.get(timeSplit[0], 0) + 1
        # sentAddressCount[splitLine[1]] = sentAddressCount.get(splitLine[1], 0) + 1

sortedSentHours = dict(sorted(sentHours.items()))

for key,value in sortedSentHours.items():
    print(key, value)
    # for key, value in time:
        # print(key, value)
