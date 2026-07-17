"""
Sum of Cubes Calculator

This script calculates the sum of the cubes of all integers between 
a starting number (m) and an ending number (n), inclusive.
"""
def sum_of_cubes_m_to_n(m, n):
    sum=0
    for i in range(m,n+1):
       sum+=i*i*i 
    print(sum)


m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))
sum_of_cubes_m_to_n(m, n)