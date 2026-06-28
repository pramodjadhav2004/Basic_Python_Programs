num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
n=int(input("Enter number to remove: "))
L=[]
for i in num_list:
    temp=list(i)
    if n in temp:
        temp.remove(n)
    L+=[tuple(temp)]
print(L)
