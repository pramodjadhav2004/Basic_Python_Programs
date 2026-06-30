m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
sq =[]
flag = 0
for i in range(m,n+1):
    for j in range(i):
        if i == j*j:
            sq+=[i]
            flag = 1
if flag == 0:
    print("No Perfect Square")
else:
    print(sq[0])
