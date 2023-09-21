import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url='http://py4e-data.dr-chuck.net/known_by_Hashim.html'
#position = int(input('Position - '))
position=18
#repeats = int(input('Repeats - '))
repeats=7
count = 0

# Retrieve all of the anchor tags
while (count+1)<=repeats:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = str(tags[position - 1].get('href', None))
    count = count + 1
    print("Retrieving:",url) 