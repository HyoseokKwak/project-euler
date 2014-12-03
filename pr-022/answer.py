
import re

f = open('names.txt')
line = f.readline()
line = re.sub('\"([A-Z]+)\"', r'\1', line)
nameList = line.split(',')
sortedNameList = sorted(nameList)
# print sortedNameList

i = 0
acc = 0
while i < len(sortedNameList):
  sum = 0
  for c in list(sortedNameList[i]):
    sum += ord(c)-64
  acc = acc + (sum*(i+1))
  i += 1
print acc
