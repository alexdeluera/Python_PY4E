# In this assignment you will write a Python program somewhat similar 
# to http://www.py4e.com/code3/geoxml.py. The program will prompt for 
# a URL, read the XML data from that URL using urllib and then parse 
# and extract the comment counts from the XML data, compute the sum of 
# the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url='http://py4e-data.dr-chuck.net/comments_1821289.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

#tree = ET.fromstring(data)
counts=ET.fromstring(data).findall('.//count')
count=0
sum=0

for item in counts:
    count+=1
    sum+=int(item.text)

print(count)
print(sum)
