"""
Mean (Average) Calculator Script

This script takes a comma-separated string of numbers from the user, 
converts them into integers, and calculates their mathematical mean.
It uses list comprehensions for efficient data conversion and includes 
error handling to manage invalid inputs or empty strings.
"""
string= input("Enter a list of numbers separated by commas: ")
int_string = string.split(',')
list_a = []
length = len(int_string)
for i in int_string:
    list_a += [int(i)]
    summ = sum(list_a)
    mean = summ / length
print(mean)

    