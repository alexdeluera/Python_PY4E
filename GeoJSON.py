import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = ''
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    url = url + urllib.parse.urlencode(parms)
    uh = urllib.request.urlopen(url, context=ctx)
    print('Retrieving', url)
   
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    placeID = js['results'][0]['place_id']
    print('Place ID is:',placeID)
