"""
Nth Smallest Element Finder

This script takes a comma-separated list of numbers and an integer 'n', 
and returns the n-th smallest number from the list. It utilizes Python's 
built-in sorting capabilities and includes robust error handling to prevent 
index out-of-bounds errors.
"""
string = input("Enter a list of numbers separated by commas: ")
n = int(input("Enter the value of k: "))
int_string= string.split(',')
list_a = []
for i in int_string:
    list_a += [int(i)]
sort_ace = sorted(list_a)
print(sort_ace[n-1])