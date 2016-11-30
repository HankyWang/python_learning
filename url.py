import urllib2
handle = urllib2.urlopen('http://1.projectzero.applinzi.com/google.html')
for line in handle:
  print line