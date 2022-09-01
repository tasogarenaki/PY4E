import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print('Retrieving:', url) 

for tag in range(count):
    # Retrieve all of the anchor tags
    tags = soup('a')
    # get infomation with tags(<a..) on position x
    link = tags[position-1].get('href', None)
    # open the url of this link
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('Retrieving:', link)    

