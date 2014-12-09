

start = 3
between = 2

list = [1]

for i in range(1, 501):
  between = i * 2
  print start
  list.append(start)
  list.append(start + between)
  list.append(start + 2*between)
  list.append(start + 3*between)
  start = start + 8 * i + 2

print sum(list)
