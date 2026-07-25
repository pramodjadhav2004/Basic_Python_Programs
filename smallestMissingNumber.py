"""
Given a list of numbers, write a program to print the smallest positive integer
missing in the given numbers.
"""
num_str=input("Enter the numbers separated by spaces: ").split()
num=set(map(int,num_str))
for i in range(1,len(num_str)+1):
    if i not in num:
        print(i)
        break