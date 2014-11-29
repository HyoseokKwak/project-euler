def d(n):
  array = []
  i = 1
  while i < n:
    if n % i == 0:
      # print i
      array.append(i)
    i += 1
  return sum(array)

def d2(n):
  return sum([i for i in range(1, n) 
      if n % i == 0])




def isPrime(n):
  i = 2
  while (i < round(n /2)):
    if (n % i == 0):
      return False
    i += 1
  return True

def d3(n):
  i = 2
  result = []
  while i <= n:
    ii = 1
    while n % i == 0:
      n = n / i
      ii *= i
    if 1 != ii:
      result.append(ii)
    i += 1
  return result

memo = {}

def sum2(n):
  if n in memo:
    return memo[n]

  memo[n] = sum([i for i in range(1, n+1) 
      if n % i == 0])
  return memo[n]

def mul(n):
  mu = 1
  for i in map(sum2, d3(n)):
    mu *= i
  return mu - n

aliquotSumMap = {}
for i in range(1, 20001):
  if isPrime(i):
    continue
  s = mul(i)

  if s > 1 and i != s:
    aliquotSumMap[i] = s

print sum([i for i in aliquotSumMap
        if aliquotSumMap[i] in aliquotSumMap and i == aliquotSumMap[aliquotSumMap[i]]])
  






aliquotSumMap = {}
for i in range(1, 10001):
  s = d2(i)
  if s > 1 and i != s:
    aliquotSumMap[i] = s

print sum([i for i in aliquotSumMap
        if aliquotSumMap[i] in aliquotSumMap and i == aliquotSumMap[aliquotSumMap[i]]])


'''
# python
def getDivisors(N):
    divisors = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisors += [i, N/i]
    return sorted(list(set(divisors)))


def isAmicable(a, b):
    return a < b and a == sum(getDivisors(b))-b
    
print sum([
  sum([i, sum(getDivisors(i))-i]) 
  for i in range(1,10001) 
    if isAmicable(i, sum(getDivisors(i))-i)])

'''
