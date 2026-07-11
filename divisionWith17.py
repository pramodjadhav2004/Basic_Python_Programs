#This program takes an integer input 'n' from the user, which represents the number of subsequent integers the user will input. It then collects 'n' integers into a list called 'num'. For each integer in the list, it calculates the integer division of that number by 17 and prints the result.
n=int(input("Enter n: "))
num=[]
for i in range(0,n):
    num.append(int(input("Enter num: ")))
for i in num:
    ans=i//17
    print(ans)