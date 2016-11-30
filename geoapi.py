import json
import urllib

address = raw_input('Enter location: ')
url = 'http://python-data.dr-chuck.net/geojson?'+urllib.urlencode({'sensor':'false','address':address})
print 'Retrieving:',url
data = urllib.urlopen(url).read()
print 'Retrieved:',len(data),'characters'

try:
  info = json.loads(str(data))
except:
  info = None

if info['status'] == 'OK':
  print 'Place id',info['results'][0]['place_id']
