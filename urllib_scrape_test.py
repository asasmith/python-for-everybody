import urllib.request, urllib.parse, urllib.error

filehandle = urllib.request.urlopen('https://asasmith.dev')

for line in filehandle:
    print('>>>', line.decode().strip())
