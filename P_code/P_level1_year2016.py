a = 5
b = 24

#방법 1
import datetime
week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
print(week[datetime.datetime(2016,a,b).weekday()])

#방법 2
month = [31,29,31,30,31,30,31,31,30,31,30,31]
week = ["FRI","SAT","SUN", "MON","TUE","WED","THU"]
print(week[((sum(month[:a-1])+b)%7)-1])

