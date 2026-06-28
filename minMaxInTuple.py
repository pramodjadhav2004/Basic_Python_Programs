n=int(input())
def convert_int(L):
    numL=[]
    for i in L:
        numL+=[int(i)]
    return numL
mainL=[]    
tuple_a=[]
list1=[]
list2=[]
for i in range(n):
    L=input().split()
    intL=convert_int(L)
    mainL+=[intL]
for i in mainL:
    list1+=[i[0]]
    list2+=[i[1]]
tuple_a.append(max(list1))
tuple_a.append(min(list1))
print(tuple(tuple_a))
tuple_a.clear()
tuple_a.append(max(list2))
tuple_a.append(min(list2))
print(tuple(tuple_a))

    