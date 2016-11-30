import urllib
import json


url = raw_input("Enter the location: ")
data = urllib.urlopen(url).read()

if len(data) != 0 :
  print 'Retrieving',url
  print 'Retrieved',len(data),'characters'
  info = json.loads(data)
  count = 0
  ans = 0
  for item in info['comments']:
    count += 1
    ans += int(item['count'])
  print 'Count:',count
  print 'Sum:',ans