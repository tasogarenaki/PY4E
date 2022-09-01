import os
os.chdir('/Users/Terry/Desktop')



name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)



counts = dict()

for line in handle:
    words = line.rstrip()
    if not words.startswith('From '):
        continue

    words = line.split()  
    time = words[5].split(':')
    hour = time[0]
    counts[hour] = counts.get(hour,0) + 1

for k,v in sorted((counts.items())):
    print(k,v)
