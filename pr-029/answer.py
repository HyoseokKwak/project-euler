import time

begin = time.time()
list = []
for a in range(2,101):
  for b in range(2,101):
    if a ** b not in list:
      list.append(a**b)

print len(list)
print time.time() - begin


begin = time.time()
s = set()
for a in range(2,101):
  for b in range(2,101):
      s.add(a**b)

print len(s)
print time.time() - begin
