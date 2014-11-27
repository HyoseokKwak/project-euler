
def tri(n):
  return n * (n+1) /2

def anum2(n):
  
  i = 2
  mulchasu = 1
  while i <= n:
    chasu = 1
    while (n % i == 0):
      n = n / i
      # print n
      chasu += 1
    i += 1
    mulchasu = mulchasu * chasu

  return mulchasu


print anum2(6)
print anum2(28)

# print tri(3)
# print tri(4)
# print tri(5)
# print tri(6)
# print anum(tri(7))
  

i = 200
target = 500
while True:
  # s += i
  # if target <= anum(s):
  t = tri(i)
  # print t
  an = anum2(t)
  # print an


  if target <= an:
    print i
    print t
    print an
    break

  i += 1


