import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

spanTags = soup('span')

count = 0

for tag in spanTags:
    num = int(tag.string)
    count = count + num

print('Sum', count)
