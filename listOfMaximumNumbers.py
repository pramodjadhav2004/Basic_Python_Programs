n=int(input("Enter n: "))
L1=[]
maximum=[]
def convert_int(L):
    L3=[]
    for i in L:
        L3+=[int(i)]
    return L3
    
for i in range(n):
    L2=input("Enter number sequence: ").split()
    L1=convert_int(L2)
    maximum.append(max(L1))
print(maximum)