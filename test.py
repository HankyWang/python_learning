import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
position = raw_input('Enter position: ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
tags = soup('a')
print 'Retrieving: '+url

s = 0

while (s < int(count)):
  s += 1
  url = tags[int(position) - 1]['href']
  print 'Retrieving: '+url
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html,'html.parser')
  tags = soup('a')