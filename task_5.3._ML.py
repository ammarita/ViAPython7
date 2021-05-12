import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'https://nominatim.openstreetmap.org/reverse?'
osm_format = 'geojson'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    lat = input('Enter latitude: ')
    lon = input('Enter longitude: ')

    url = serviceurl + urllib.parse.urlencode({'lat': lat, 'lon': lon, 'format': osm_format})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'features' not in js:
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    location = js['features'][0]['properties']['display_name']
    print(location)