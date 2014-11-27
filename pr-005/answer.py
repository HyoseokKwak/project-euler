'''
def div(number):
  for i in range(2, 21):
    if 0 != number % i:
      return False
  return True

i = 210000000
while True:
  if(True == div(i)):
    print i
    break
  i += 1
'''

# euclidean algorithm
def gcd(a,b):
  if (0 == b):
    return a
  return gcd(b, a%b)

def lcm(a, b):
  c = abs(a * b);
  return c / gcd(a,b)

l = 1
for i in range(1,21):
  l = lcm(l, i)

print l 
