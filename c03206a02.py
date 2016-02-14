import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'


address = raw_input('Enter location: ')
if len(address) < 1 : exit()

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#print url
#exit()
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None
if 'status' not in js or js['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    print data
    exit()


#print len(js["results"])
#print type(js["results"])
#exit()
pid=js['results'][0]['place_id']

print pid
