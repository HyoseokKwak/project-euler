

def fibo(a, b, sum):

  if(a > 4000000):
    return sum

  if a % 2 == 0:
    sum = sum + a

  return fibo(b, a+b, sum)


print fibo(1,2,0)


