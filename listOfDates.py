"""
You are given two dates D1 and D2.
Write a program to print the list of dates between two dates D1 and D2(including
D1 and D2) in the increasing order of the dates.
The date in string format is like "Feb 20 2021".
"""
import datetime
def days_print(dt1,dt2,delta):
    if dt1==dt2:
        print(dt1)
        return
    print(dt1)
    dt1=dt1+delta
    return days_print(dt1,dt2,delta)
date1=input("Enter the first date in string format (e.g., 'Feb 8 2021'): ")
date2=input("Enter the second date in string format (e.g., 'Feb 8 2021'): ")
dt1=datetime.datetime.strptime(date1,"%b %d %Y")
dt2=datetime.datetime.strptime(date2,"%b %d %Y")
delta=datetime.timedelta(days=1)
days_print(dt1,dt2,delta)