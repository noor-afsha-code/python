"""
Write a program to calculate car park charges. 
Up to 2 hours costs £3.50, up to 4 hours £5.00, up to 12 hours £10.00.
The driver enters the number of hours they require and the machine prints the current time,
expiry time and charge. For example:

Time now: Wed Oct 7 15:47:46 2020

Expires: Thu Oct 8 03:47:46 2020

Charge = 10.00
"""
"""
WECLCOME TO THE PARKING LOT ABC
PRINT THE DETAILS: <= 2HRS: 3.5£, 2-4 = 5.00, 4-12 = 10
iNPUT FROM USER: hours to stay
machine prints: expiry time and charge
time now and expiry time with date
"""

#importing current time and date

"""
#Current_time= time.time()--> imports time in seconds 

import time
current_time = time. time()
print(f"Current time: {current_time}")
#Current time: 1748427886.2310479
"""


#The following time.ctime() produces non-summer-time. with date.

"""
import time
current_time = time.ctime()
print(f"current time:{current_time} ")
#current time:Wed May 28 10:23:04 2025 : ACTUAL TIME IS 11:23:04
"""

#getting time and date with summer-time using time.localtime(). NO SUMMER TIME

"""
import time
current_time = time.gmtime()
print(f"Current Time: {current_time}")

#Current Time: time.struct_time(tm_year=2025, tm_mon=5, tm_mday=28, tm_hour=10, tm_min=19, tm_sec=8, tm_wday=2, tm_yday=148, tm_isdst=0)
"""

#NO SUMMER TIME
"""
import time
current_time = time.localtime()
print(f"Current Time: {current_time}")
# Current Time: time.struct_time(tm_year=2025, tm_mon=5, tm_mday=28, tm_hour=10, tm_min=21, tm_sec=28, tm_wday=2, tm_yday=148, tm_isdst=0)
"""
"""
import time
CurrentTime = time.time()
current_time = time.ctime(CurrentTime)
print(f"time: {current_time}")

#time: Wed May 28 10:32:11 2025
"""

#importing date and time as per the local zone with the time correction

#datetime and pytz helps in determining the local time with any corrections needed
from datetime import datetime
import pytz

#define the timezone in ''. 
timezone = pytz.timezone('europe/london')

#get the current time with the correction
current_time = datetime.now(timezone)

#the default gives the total hours with plus one in the end. 
# To get the desired format type {%Y(for year-%m (for month-%d(for day) SPACE
# %H(for hours):%M (for minutes):%S(for seconds) %Z defines BST or British SUmmer Time}

print(f"Local Time: {current_time.strftime("%Y-%m-%d %H:%M:%S %Z")}")

#pytz to define a specific time zone. 
#Gets the current time with the correct summer time adjustment. 
#Displays the time, including the timezone abbreviation (BST for British Summer Time).


