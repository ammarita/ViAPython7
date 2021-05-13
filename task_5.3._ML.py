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
    lat = input('Enter latitude (range -90 to 90): ')
    lon = input('Enter longitude (range -180 to 180): ')

    url = serviceurl + urllib.parse.urlencode({'lat': lat, 'lon': lon, 'format': osm_format})
    print('Calling: ', url)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'features' not in js:
        print('Something went wrong:')
        print(data)
    else:
        try:
            name = js['features'][0]['properties']['name']
        except:
            name = 'None'
            pass
        try:
            type = js['features'][0]['properties']['type']
        except:
            type = 'None'
            pass
        try:
            country_name = js['features'][0]['properties']['address']['country']
        except:
            country_name = 'None'
            pass
        try:
            country_code = js['features'][0]['properties']['address']['country_code']
        except:
            country_code = 'None'
            pass
        print('You searched a place with coordinates: latitude -', lat, 'longitude -', lon, 
        '\nPlace name:', name, '\nType of the place:', type, '\nCountry:', country_name, 
        '(',country_code.upper(),')')

    while True:
        repeat = input('Repeat (Y/N)?')

        if repeat.upper() == 'Y':
            break
        elif repeat.upper() == 'N':
            exit()
        else:
            print('Unsupported input')
            continue