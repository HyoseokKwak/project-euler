

import math

fac = math.factorial(100)

facArray = [ (int(single)) for single in str(fac)]
s = sum(facArray)

fac2 = map(lambda single: int(single), list(str(fac)))
s2 = sum(fac2)

print facArray
print s
print s2
