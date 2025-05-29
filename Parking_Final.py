"""
WELCOME TO THE PARKING LOT ABC
HOURLY RATE
CURRENT TIME:
HOURS SELECTED
TIME EXPIRES AT:
TOTAL PAYBALE AMOUNT
"""
#welcome message plus charging information

print("WELCOME TO THE PARKING LOT ABC")
print(f"Parking Charges: \n upto 2 hours: £3.50\n upto 4 hours: £5.00\n upto 12 hours: £10.00")

#prompt for user to enter the number of required hours

parking_hours = int(input("Enter the number of hours for parking: "))


#fetching the current time for local summer time using datetime and pytz
#timedelt for adding or subtracting hours in the time

from datetime import datetime, timedelta 
import pytz

#define timezone
timezone = pytz.timezone('europe/london')
current_time = datetime.now(timezone)
print(f"Current Local time: {current_time.strftime("%Y-%m-%d %H-%M-%S %Z")}")

#calculating charges #calculating the total time using datetime, timedelta (to add extra hours) and time modules

if parking_hours <= 2:
    total_charges = 3.5
    total_time = current_time + timedelta(hours=2)
elif 2< parking_hours<=4:
    total_charges = 5
    total_time = current_time + timedelta(hours=4)
elif parking_hours <= 12:
    total_charges = 10
    total_time = current_time + timedelta(hours=12)

print(f"Expiry Time: {total_time.strftime("%Y-%m-%d %H-%M-%S %Z")}\n Total charges:£{total_charges}")



