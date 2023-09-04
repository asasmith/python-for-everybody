import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter - ')
response = urllib.request.urlopen(url).read().decode()

data = json.loads(response)
commentsList = data['comments']

sum = 0

for item in commentsList:
    countInt = int(item['count'])
    sum = sum + countInt

print(sum)

