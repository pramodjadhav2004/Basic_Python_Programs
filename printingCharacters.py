# This program takes two integer inputs from the user representing starting and ending Unicode values, and prints the characters corresponding to those Unicode values.
m=int(input('Enter the starting Unicode value: '))
n=int(input('Enter the ending Unicode value: '))
for i in range(m,n+1):
    print(chr(i))