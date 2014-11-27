
def isPalindrome(number):
  return str(number) == str(number)[::-1]


max = 0
for i in range(100, 1000):
  for j in range(100, 1000):
    mul = i * j 
    if ( isPalindrome(mul) and mul > max ):
      max = mul
print max




print max([x*y 
  for x in range(100, 1000) 
    for y in range(x, 1000) 
      if str(x*y) == str(x*y)[::-1]])
