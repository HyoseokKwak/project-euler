

print 2**15
num = 2**15


num = 2**1000
sum = 0
while num > 0:
  sum += num % 10
  num = num / 10

print sum
