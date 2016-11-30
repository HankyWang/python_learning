import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter location: ")

data = urllib.urlopen(url).read()

print 'Retrieving',url
print 'Retrieved',len(data),' characters'

count = 0
ans = 0
tree = ET.fromstring(data)
res = tree.findall('.//count')
for item in res:
  count += 1
  ans += int(item.text)
print 'Count:', count
print 'Sum:', ans