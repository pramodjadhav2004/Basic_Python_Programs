"""
Write a program to convert the date given in the string format to a datetime object.

The date in string format is like "8 Feb 2021".
"""
from datetime import datetime
string_date = input()
date_time = datetime.strptime(string_date, "%d %b %Y")
print(date_time)