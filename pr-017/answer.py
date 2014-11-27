
word = {}
word[0] = '' 
word[1] = 'one' 
word[2] = 'two' 
word[3] = 'three' 
word[4] = 'four' 
word[5] = 'five' 
word[6] = 'six' 
word[7] = 'seven' 
word[8] = 'eight' 
word[9] = 'nine' 
word[10] = 'ten' 
word[11] = 'eleven' 
word[12] = 'twelve' 
word[13] = 'thirteen' 
word[14] = 'fourteen' 
word[15] = 'fifteen' 
word[16] = 'sixteen' 
word[17] = 'seventeen' 
word[18] = 'eighteen' 
word[19] = 'nineteen' 
word[20] = 'twenty' 
word[30] = 'thrity' 
word[40] = 'fourty' 
word[50] = 'fifty' 
word[60] = 'sixty' 
word[70] = 'seventy' 
word[80] = 'eighty' 
word[90] = 'ninty' 

def sayWord(a):
  if a in word:
    return word[a]
  else:
    c = a / 10
    d = a % 10
    w = ''
    if 0 < c:
      w = word[c*10]
    if 0 < d:
      w += word[d]
    return w

def lenNumberToWord(n):
  a = 0
  b = 0

  length = 0

  if n >= 100:
    a = n / 100
    b = n % 100
    length += len(sayWord(a))
    length += len('hundred')
    if(b > 0):
      length += len('and')
      length += len(sayWord(b))
  else:
    length += len(sayWord(n))

  return length


# print lenNumberToWord(20)
# print lenNumberToWord(21)
# print lenNumberToWord(121)
# print lenNumberToWord(171)
# print lenNumberToWord(115)
# print lenNumberToWord(100)
# print lenNumberToWord(342)

i = 1
ss = 0
while i < 1000:
  ss += lenNumberToWord(i)
  i += 1
ss += len('onethousand')

  
print ss

  
def tostr(N):
    if N == 1000:
        return 'onethousand'
    elif N >= 100:
        if N % 100 == 0: return tostr(N/100)+'hundred'
        else:            return tostr(N/100)+'hundredand' + tostr(N%100)
    elif N >= 20:    
        return ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty'][N/10-2]+tostr(N%10)
    else:
        return ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][N]

print sum([len(tostr(n)) for n in range(1, 1001)])
