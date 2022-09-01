import os
os.chdir('/Users/Terry/Desktop')


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue

    count = count + 1
    find_email = line.split()
    print(find_email[1])
    
print("There were", count, "lines in the file with From as the first word")

