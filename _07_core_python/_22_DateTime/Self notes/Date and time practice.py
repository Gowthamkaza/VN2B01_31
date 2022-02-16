import calendar
import datetime
#Import the datetime module and display the current date:
x=datetime.datetime.now()
print(x)

print(x.year)


import time
# Getting current time
localtime=time.localtime(time.time())
print("local current time",localtime)


# Getting formatted time
# simple method to get time in readable format is asctime()
localtime2=time.asctime(time.localtime(time.time()))
print(localtime2)

#Getting calendar for a month
cal1=calendar.month(2022,2)
print(cal1)





