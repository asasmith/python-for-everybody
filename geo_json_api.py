import urllib.request, urllib.parse, urllib.error
import json

locationInput = input('Enter Location - ')
base_url = 'http://py4e-data.dr-chuck.net/json?'

if len(locationInput) < 1:
    print(locationInput)
    print('location invalid')
    quit();

params = dict()
params['address'] = locationInput
params['key'] = 42
url = base_url + urllib.parse.urlencode(params)

response = urllib.request.urlopen(url).read().decode()

data = json.loads(response)


if not data or 'status' not in data or data['status'] != 'OK':
    print('Server error')
    quit()

place_id = data['results'][0]['place_id']
    
print(place_id)

