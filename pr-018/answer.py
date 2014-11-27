input='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

ll = map(
      lambda str: 
        map(int,str.split(' ')),
      input.split('\n'))

# print ll

# l = [item 
#     for sublist in ll
#       for item in sublist]
# print l


# pos = 0
# for i in range (1, 3):
#   print i
#   orig = b[pos + i - 1]
#   print orig
#   for j in range(i+1):
#     print pos + +i - 1 + i + j
#   pos += i

def takeMax(numberList):
  i = 0
  newList = []
  while i < len(numberList):
    newList.append( max(numberList[i], numberList[i + 1]))
    i += 2

  return newList
  
sumArray = [75]

for i in range(1, 15):
  newSumArray = []
  for j in range(i):
    print '%s + %s %s' % (sumArray[j],  ll[i][j], ll[i][j+1])
    newSumArray.append(sumArray[j] + ll[i][j])
    newSumArray.append(sumArray[j] + ll[i][j+1])
      
  print newSumArray
  sumArray = []
  sumArray.append(newSumArray[0])
  sumArray.extend(takeMax(newSumArray[1:-1]))
  sumArray.append(newSumArray[-1])
  print sumArray

print max(sumArray)



aa = [187, 217, 186, 124, 202, 221]

print takeMax(aa[1:-1])





# #!/usr/bin/env python
 
# import time
 
# # define a recursive function to create partial sums by row
# def recSumAtRow(rowData, rowNum):
#     # iterate over the given row
#     for i in range(len(rowData[rowNum])):
#         # add the largest of the values below-left or below-right
#         rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
#     # base case
#     if len(rowData[rowNum])==1: return rowData[rowNum][0]
#     # recursive case
#     else: return recSumAtRow(rowData, rowNum-1)
 
# # read in the data
# rows = []
# # with open('problem-18-data') as f:
# #     for line in f:
# #         rows.append([int(i) for i in line.rstrip('\n').split(" ")])
 
# def toInt(str):
#   return int(str)

# ll = map(lambda str: map(int, str.split(' ')) ,input.split('\n'))
 
# start = time.time()
# result = recSumAtRow(ll, len(ll)-2) # start at second to last row
# elapsed = time.time() - start
 
 
# print "%s found in %s seconds" % (result ,elapsed)
