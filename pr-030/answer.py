

'''
list = []
for a in range(0, 10):
  for b in range(0, 10):
    for c in range(0, 10):
      for d in range(0, 10):
        for e in range(0, 10):
          if a**5 + b**5 + c**5 + d**5 + e**5 == int('%d%d%d%d%d'%(a,b,c,d,e)):
            list.append( int('%d%d%d%d%d'%(a,b,c,d,e)))
print sum(list)
'''

list = []
i = 2
while True:
  s = 0
  for c in str(i):
    s += int(c) ** 5 

  if s == i:
    # print i
    list.append(i)

  if i >= 999999:
    break

  i += 1

print sum(list)


