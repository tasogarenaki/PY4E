import os
os.chdir('/Users/Terry/Desktop')


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
new = list()
count = 0 
for line in fh:
    line = line.rstrip()
    lst.append(line)
    new = new + lst[count].split() 
    count = count + 1 


new = list(set(new))
new.sort()
print(new)