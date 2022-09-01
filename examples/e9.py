import os
import re
os.chdir('/Users/Terry/Desktop')


name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1250237.txt"
handle = open(name)

total = 0

for line in handle:
    number = line.rstrip()
    final = re.findall('[0-9]+',number)

    for k in range(len(final)):
        total = total + int(final[k])

print(total)





