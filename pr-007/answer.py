primeArray = [2]


def isPrime(n):
  i = 2
  while (i < round(n /2)):
    if (n % i == 0):
      return False
    i += 1
  return True


def isPrime2(n):
  for i in primeArray:
    if (n % i == 0):
      #print 'not %d, %d' % (n, i)
      return False

  primeArray.append(n)
  #print 'insert %d' % (n)
  #print primeArray
  return True

j = 2
count = 0

targetCount = 10001
while True:
  if isPrime2(j):
    count += 1
    if count == targetCount - 1:
      print j
      break;
  j += 1


