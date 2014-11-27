import math

n = 600851475143

def findN(num):
  sn = int(round(math.sqrt(n)))
  print sn

  i = 1
  #while (i < sn):
  while (i < num):
    if (num % i == 0):
      num = num / i
      print i
    i += 1
  print num

findN(n)


