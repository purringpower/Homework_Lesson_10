import os
import datetime


# 1
print(os.path.abspath(os.curdir))

# 2

my_date =input("Your date:")
day, month, year = (int(x) for x in my_date.split('.'))
ans = datetime.date(year, month, day)
print(ans.strftime("%A"))

print(ans.isocalendar()[1])
