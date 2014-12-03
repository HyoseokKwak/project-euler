'''
def d(n):
  array = []
  i = 1
  while i < n:
    if n % i == 0:
      # print i
      array.append(i)
    i += 1
  return array

def isPrime(n):
  i = 2
  while (i < round(n /2)):
    if (n % i == 0):
      return False
    i += 1
  return True

exceed = []

i = 2
while i <= 28123:
  if isPrime(i):
    i += 1
    continue

  if sum(d(i)) > i:
    exceed.append(i)
  
  i += 1

print ','.join([str(x) for x in exceed])
'''

readLine = open("exceed.txt").readline()

exceeds = [int(x) for x in readLine.split(',')]
    
# print exceeds

sumArray = {}
for a in exceeds:
  for b in exceeds:
    sumArray[a+ b] = 1

i = 1
s = 0
while i <= 28123:
  if i not in sumArray:
    s += i
  i += 1

print s






