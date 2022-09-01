import urllib.request, urllib.parse, urllib.error
import json





address = input('Enter location: ')

url = address 
print('Retrieving', url)
uh = urllib.request.urlopen(url)


data = uh.read()
print('Retrieved', len(data), 'characters')


info = json.loads(data)
print('Count:',len(info["comments"]))

sum = 0
# direct use info["comments"], cause 'count' inside of it
for item in info["comments"]:

  sum += int(item['count'])

print(sum)
