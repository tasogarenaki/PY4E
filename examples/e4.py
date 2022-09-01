import os
os.chdir('/Users/Terry/Desktop')


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
n4 = 0
count = 0 
for line in fh:
    # search for text with "X-DSPAM-Confidence:" from the file
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # fine the number after : and sum()
    n1 = line.find(':')
    n2 = line[n1+1:]
    n3 = float(n2)
    n4 = n4 + n3
    count = count +1 
# calculate the average
final = float(n4/count)
print('Average spam confidence:', final)
