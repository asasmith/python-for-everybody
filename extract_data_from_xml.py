import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')
print('Retrieving', url)
response = urllib.request.urlopen(url).read()

print(response)

tree = ET.fromstring(response)

counts = tree.findall('.//count')

sum = 0

for item in counts:
    itemToNum = int(item.text)
    sum = sum + itemToNum

print(sum)

