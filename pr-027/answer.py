

def isPrime(n):
  return n in primeArray


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



def expression(a,b):
  i = 1
  while True:
    if not isPrime(i**2 + a*i + b):
      return i - 1
    i += 1


def primes_xrange(stop):
  primes = [True] * stop
  primes[0], primes[1] = [False] * 2
  for ind, val in enumerate(primes):
    if val is True:
      primes[ind*2::ind] = [False] * (((stop - 1)//ind) - 1)
  return primes
 
print primes_xrange(100)
print prime_sieve(100)
 
P = primes_xrange(751000)
primeArray = prime_sieve(751000)


# http://code.jasonbhill.com/sage/project-euler-problem-27/

import time

start = time.time()
max = 0
a_max, b_max, c_max = 0,0,0

for a in range(-1000, 1001):
  b = 1
  for b in range(1, 1001):

    # B should be prime, since n=0 must result in a prime.

    if P[b] is False: continue
    # if b not in primeArray: continue

    # if b < -1600-40*a or b < c_max: continue

    c,n = 0,0
    while P[n**2 + a*n + b] is True:
      c += 1
      n += 1
    if c > c_max:
      a_max, b_max, c_max = a, b, c

prod = a_max * b_max

elapsed = time.time() - start
print "a=%s, b=%s, longest sequence = %s, prod=%s\nfound in %s seconds"\
% (a_max, b_max, c_max, prod, elapsed)

