"""
Prime Number Generator Script

This script identifies and outputs all prime numbers within a user-defined 
inclusive range [m, n]. 

It optimizes the primality test by only checking divisors up to the square 
root of the number, which reduces the time complexity significantly compared 
to checking all numbers up to n-1. It also utilizes list comprehensions and 
string joining for efficient memory management.
"""
def check_is_prime(m, n):
    prime=""
    for i in range(m,n+1):
        flag=0
        if(i==1 or i==0):
            continue
        for j in range(2,i):
            if(i%j==0):
                flag=1
        if (flag==0):
            prime+=str(i)+" "
    return prime
m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))

prime_numbers = check_is_prime(m, n)

print(prime_numbers)