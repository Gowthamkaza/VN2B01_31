from datetime import datetime, timedelta
from pytz import timezone
import pytz

utc = pytz.utc
print("UTC Zone : ", utc.zone)
eastern = timezone('US/Eastern')  # 'US/Eastern'
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
loc_dt = eastern.localize(datetime(2011, 8, 10, 8, 54, 0))
print(loc_dt.strftime(fmt))



# to print calender

import calendar

yy = int(input("Enter year in YYYY: "))

# display the calendar
print(calendar.calendar(yy))