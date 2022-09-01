import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

# useless
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# compute the sum of the numbers in the file and enter the sum
# the numbers are inside tag 'count'

address = input('Enter location: ')

url = address 
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)


data = uh.read()
print('Retrieved', len(data), 'characters')


tree = ET.fromstring(data)
sum = 0
# locatate 'count' and find them all
counts = tree.findall('.//count')
print('Count:', len(counts))

for count in counts:
    # the numbers are 'text' from count
    sum += int(count.text)

print(sum)