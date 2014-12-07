def fib1(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = 1
    else:
        memo[n] =  fib1(n-1) + fib1(n-2)
    return memo[n]


def fib(n):
  def fib_help(a, b, n):
    return fib_help(b, a+b, n-1) if n > 0 else a
  return fib_help(0, 1, n) 


memoryMap = {}

def fibMap(n):
  if n in memoryMap:
    return memoryMap[n]

  if (n <= 1):
    memoryMap[n] = n
  else:
    memoryMap[n] = fibMap(n-1) + fibMap(n-2)

  return memoryMap[n]

i = 1
while i < 100000000000:
  n = fibMap(i)
  if len(str(n)) == 1000:
    print i
    break
  i += 1
  

