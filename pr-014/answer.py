
memo = {}

def collattz(n):
  start = n
  count = 1
  # print n
  while n > 1:
    if 0 == n % 2 :
      n = n / 2
    else:
      n = 3 * n + 1

    if n in memo:
      # print "in %d, %d" % (n, count)
      # print "in %d, %d" % (n, count + memo[n])
      return count + memo[n]

    count += 1

  # print "%d, %d" % (start, count)
  return count



m = 0
max = 0
number = 0
n = 1000000
while n > 0:
  m = collattz(n)
  memo[n] = m

  if(max < m):
    max = m
    number = n
  n -= 1
  

print "number %d, max %d" % (number, max)
