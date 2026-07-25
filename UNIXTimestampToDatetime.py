"""
The Unix timestamp is a way to track time as a running total of seconds.
This count starts at the Unix Epoch on January 1st, 1970, at UTC.
Therefore, the Unix timestamp is merely the number of seconds between a
particular date and the Unix Epoch.
You are given UNIX timestamp U.
Write a program to convert U to a readable date time(in UTC) and print it.
"""
import datetime
seconds=int(input("Enter the UNIX timestamp: "))
second_obj=datetime.datetime.strptime("Jan 01 1970","%b %d %Y")
delta=datetime.timedelta(days=seconds/86400)
print(second_obj+delta)