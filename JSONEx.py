import urllib.request, urllib.parse, urllib.error
import json
count=0
sum=0

url = 'http://py4e-data.dr-chuck.net/comments_1821290.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data=uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)

for item in info['comments']:
    count+=1
    sum+=int(item['count'])

print('Count: ',count)
print('Sum: ',sum)
