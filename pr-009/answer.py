import math

def isPitagoras(a,b,c):
  return math.pow(c,2) == math.pow(a,2) + math.pow(b,2)


print isPitagoras(3,4,5)
#print isPitagoras(1,498,501)

# a + b + c = 1000
# c = 1000 - a - b


# print reduce(
#     lambda x, y: x * y, [
#       [a, b, 1000-a-b] 
#       for a in range(1, 1001) 
#       for b in range(a, 1001) 
#       if a**2 + b**2 == (1000-a-b)**2][0])

# for a in range(1,1000):
#   for b in range(2,1000):
#     for c in range(3,1000):
#       if (a + b + c) == 1000 and a < b and b < c:
#         if isPitagoras(a,b,c):
#           print "%d, %d, %d" % (a,b,c)
#           print a*b*c
  

for a in range(1,1000):
  for b in range(a,1000):
        if isPitagoras(a,b,1000-a-b):
          print "%d, %d, %d" % (a,b,1000-a-b)
          print a*b*(1000-a-b)
