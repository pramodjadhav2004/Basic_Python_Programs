"""
Write a program to print the previous day of D, the current day D, and the next day of D.

The date in string format is like "8 Feb 2021".
"""
import datetime
cur_date =input("Enter the date in string format (e.g., '8 Feb 2021'): ")
date_obj = datetime.datetime.strptime(cur_date, "%d %b %Y")
previous = datetime.timedelta(days= 1)
print(date_obj-previous)
print(date_obj)
print(date_obj+previous)