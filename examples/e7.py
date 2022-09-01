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
    email = words[1]

    counts[email] = counts.get(email,0) + 1


bigcount = None
bigword = None


for word,count in counts.items():


    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)


