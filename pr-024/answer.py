


numbers = []
for i in range(10):
  for j in range(10):
    if(j == i):
      continue
    for k in range(10):
      if(i== k or j == k):
        continue
      for l in range(10):
        if(i== l or j == l or k == l):
          continue
        for m in range(10):
          if(i == m or j == m or k == m or l == m):
            continue
          for n in range(10):
            if(i == n or j == n or k == n or l == n or m == n):
              continue
            for o in range(10):
              if(i == o or j == o or k == o or l == o or m == o or n ==o):
                continue
              for p in range(10):
                if(i == p or j == p or k == p or l == p or m == p or n ==p or o == p):
                  continue
                for q in range(10):
                  if(i == q or j == q or k == q or l == q or m == q or n ==q or o == q or p == q):
                    continue
                  for r in range(10):
                    if(i == r or j == r or k == r or l == r or m == r or n ==r or o == r or p == r or q == r):
                      continue
                    numbers.append("%d%d%d%d%d%d%d%d%d%d" % (i, j, k, l, m, n, o, p, q, r))
              
n = sorted(numbers)

print n[0]
print n[999999]
