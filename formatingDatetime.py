"""
Write a program to convert the date in string format to another string format.

The input date string format is like "Jul 01 2014 02:43PM"
The output date string format should be like "DD/MM/YYYY HH:MM:SS"
"""
from datetime import datetime
date_str = input("Enter the date in string format (e.g., 'Jul 01 2014 02:43PM'): ")
date_time_1 = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
date_time_2 = date_time_1.strftime("%d/%m/%Y %H:%M:%S")
print(date_time_2)