"""
Median Calculator Script

This script takes a comma-separated list of numbers, sorts them, and 
calculates the statistical median. It handles both even and odd-length 
datasets appropriately.
"""
string = input("Enter a list of numbers separated by commas: ")
int_string = string.split(',')
list_a = []
count = len(int_string)

for i in int_string:
    list_a += [int(i)]
sort_ace = sorted(list_a)
if count % 2 == 0:
    ans = count // 2
    median = sum(sort_ace[-ans : -ans-2:-1]) / 2
    print(median)
else:
    ans = count // 2
    median = sort_ace[ans]
    print(median)
    
    
    
    
    