'''
# answer 1
primeArray = [2]


def isPrime2(n):
  for i in primeArray:
    if (n % i == 0):
      #print 'not %d, %d' % (n, i)
      return False

  primeArray.append(n)
  #print 'insert %d' % (n)
  #print primeArray
  return True




import math
def isPrime3(num):
  """docstring for isPrime3"""
  n = round(math.sqrt(num))
  # print "%d %d" % (num, n)

  i = 2
  while i <= n:
    if 0 == num %i:
      return False
    i += 1

  return True;
  

j = 3
while j < 2000000:
  if isPrime3(j):
    primeArray.append(j)
  j += 1

#print primeArray
print reduce(lambda x,y: x+y,  primeArray)

'''




# answer 2

rangenum = 2000000
rangenum = 10
targets = range(1,rangenum+1)
print targets


def setTombstone(number):
  if 0 == targets[number - 1]:
    return

  i = 2
  pos = number * 2 -1
  while pos < rangenum:
    targets[pos] = 0
    i += 1
    pos = number*i -1


i = 2
while i < rangenum:
  setTombstone(i)
  i += 1

#print targets
print reduce(lambda x,y: x+y,  targets) -1









'''
rangenum = 10000
targets = range(2, rangenum + 1)

# print targets

# primeArray = [2]
# def isPrime(n):
#   """docstring for isPrime"""
#   for i in primeArray:
#     if 0 == i or 0 == n % i:
#       return False

#   return True
      

def timesFilter(inputNum, num):
  i = 1
  while i < rangenum:
    if inputNum == num * i:
      return False
    i += 1

  return True




from functools import partial

primeArray = []
i = 0
while i < len(targets) and 0 < len(targets):
  #print "%d %d" % (i, len(targets))
  madenFilter = partial(timesFilter, num=targets[i])
  primeArray.append(targets[i])
  targets = filter(madenFilter, targets)
  #print targets

print primeArray
print reduce(lambda x,y: x+y,  primeArray)
'''
