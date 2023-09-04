import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

urlInput = input('Enter - ')
positionInput = input('Position - ')
repeatInput = input('Repeat - ')
repeatInt = int(repeatInput) + 1
positionInt = int(positionInput) - 1
iteration = 0

splitUrl = urlInput.split('/');
href = splitUrl.pop(3)
separator = '/'

while iteration < repeatInt:
    url = separator.join(splitUrl) + '/' + href
    print('Retrieving:', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchorTags = soup('a')
    href = anchorTags[positionInt].get('href', None)
    iteration = iteration + 1

