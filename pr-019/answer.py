from datetime import timedelta, datetime

beginDate = datetime(1901 , 1, 1)
endDate = datetime(2000, 12, 31)
oneDay = timedelta(days=1)

count = 0
while beginDate != endDate:
  
  if 1 == beginDate.day and 6 == beginDate.weekday():
    count += 1
    print beginDate

  beginDate = beginDate + oneDay

print count


## other's solutions
from calendar import monthrange, SUNDAY
print(len([
  (year, month) 
  for year in range(1901, 2001) 
    for month in range(1, 13) 
      if monthrange(year, month)[0] is SUNDAY]))


from calendar import monthrange, SUNDAY
print(len(
  [(year, month) 
  for year in range(1901, 2001) 
    for month in range(1, 13) 
      if datetime(year, month, 1).weekday() == 6]
  ))
