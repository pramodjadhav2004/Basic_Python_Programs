"""
Given date-time D, write a program to print the time left for the next New Year.
"""
import datetime
date_str=input("Enter the date and time in the format 'MMM DD YYYY HH:MM AM/PM': ")
date_obj=datetime.datetime.strptime(date_str,"%b %d %Y %I:%M %p")
current_year=date_obj.year
new_year="Jan 01 "+str(current_year+1)+" 12:00 AM"
newyear_obj=datetime.datetime.strptime(new_year,"%b %d %Y %I:%M %p")
count_down=newyear_obj-date_obj
day=count_down.days
seconds=count_down.seconds
hours=seconds//3600
minutes=(seconds%3600)//60
print("Time left for the next New Year: "+str(day*24+hours)+" hours "+str(minutes)+" minutes")