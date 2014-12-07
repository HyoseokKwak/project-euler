# print 1/6.0
# print 1/7.0

def divide(m, n):
  i = 0
  result = []
  if(n % 2 == 0):
    return result

  for i in range(n*1000):
    a = m * 10 / n 
    m = m * 10 % n 
    result.append(str(a))
    if(m == 0):
      break
  return result

def findCirculationString(target):
  maxStr = ''
  for i in range(len(target)):
    nextI = target.find(target[i], i+1)
    if (nextI > 0):
      subStrA = target[i:nextI]
      if len(target) < nextI + (nextI - i):
        continue
      subStrB = target[nextI: nextI + (nextI - i)]
      if(subStrA == subStrB):
        if(len(maxStr) < len(subStrA)):
          maxStr = subStrA
  return maxStr



# maxLength = 0
# for i in range(832, 1001):
#   a = ''.join(divide(1, i))
#   div = findCirculationString(a)
#   if maxLength < len(div):
#     maxLength = len(div)
#     print i, div, maxLength
    


def prime_sieve(n):
  """
  http://blog.dreamshire.com/common-functions-routines-project-euler/#is_prime
    Return a list of prime numbers from 2 to a prime < n. Very fast (n<10,000,000) in 0.4 sec.

    Example:
    >>>prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]

    Algorithm & Python source: Robert William Hanks

http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers

    """
  sieve = [True] * (n/2)
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i/2]:
      sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
  return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

L = 1000
primes = prime_sieve(L)

for p in primes[::-1]:
  c = 1
  while pow(10, c, p) - 1 != 0:
    c += 1
  if (p-c) == 1: break

print "Project Euler 26 Solution =", p





def circ(num):
  d = 1
  divideds = []
  while 1:
    (q, r) = (d // num, d % num)
    print d, q, r, divideds
    if d in divideds:
      return len(divideds[divideds.index(d):])
    else:
      divideds.append(d)
    d = r * 10


max = 0
maxLength = 0
for i in xrange(1, 100):
  print 'start %d' % i
  l = circ(i)
  if maxLength < l:
    max = i
    maxLength = l
print max
