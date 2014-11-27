def powsum(list):
  sum = 0
  for i in list:
    sum += pow(i,2)
  return sum

def sumpow(list):
  sum = 0
  for i in list:
    sum += i
  return pow(sum, 2)

a = 101
print sumpow(range(a)) - powsum(range(a));
