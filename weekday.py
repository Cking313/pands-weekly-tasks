# weekday.py
# Outputs whether or not it is a weekday
# Author: Colleen King
# Need datetime library to get date and time
# https://stackoverflow.com/questions/8380389/get-day-name-from-datetime
import datetime

# string format today's date as a weekday
day_name = datetime.datetime.today().strftime("%A")

# check if today is a weekend day
if day_name in ['Friday', 'Saturday', 'Sunday']:
    print('It is the weekend, yay!')
else:
    print('Yes, unfortunately today is a weekday.')