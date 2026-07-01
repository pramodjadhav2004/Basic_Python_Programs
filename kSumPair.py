L=input("Enter a list of numbers separated by spaces: ").split(",")
L1=[]
temp=[]
finalList=[]
tuple1=[]
set1=set()
sum1=int(input("Enter the target sum: "))
for i in L:
    L1+=[int(i)]
for i in L1:
    for j in L1:
        if i+j==sum1:
            tuple1.append(i)
            tuple1.append(j)
            tuple1.sort()
            temp.append(tuple(tuple1))
            tuple1.clear()
for i in temp:
    if i not in finalList:
        finalList.append(i)
        finalList.sort()
for i in finalList:
    print(i)
        
    