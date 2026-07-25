"""
Given two dates D1 and D2, write a program to count the number of Saturdays
and Sundays from D1 to D2 (including D1 and D2).
The date in string format is like "8 Feb 2021".
"""
import datetime
def check_sat_sun(dt1,dt2,delta,sat_count=0,sun_count=0):
    weekday=dt1.strftime("%A")
    if weekday=="Saturday":
        sat_count+=1
    if weekday=="Sunday":
        sun_count+=1
    if dt1==dt2:
        return sat_count,sun_count
    return check_sat_sun(dt1+delta,dt2,delta,sat_count,sun_count)
date1=input("Enter the first date in the format 'DD MMM YYYY': ")
date2=input("Enter the second date in the format 'DD MMM YYYY': ")
dt1=datetime.datetime.strptime(date1,"%d %b %Y")
dt2=datetime.datetime.strptime(date2,"%d %b %Y")
delta=datetime.timedelta(days=1)
sat_count,sun_count=check_sat_sun(dt1,dt2,delta)
print("Saturday: "+str(sat_count))
print("Sunday: "+str(sun_count))