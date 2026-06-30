index=input("Enter the dimensions of the matrix (m n): ").split()
m=int(index[0])
n=int(index[1])
main_list=[]
def int_list(row):
    row1=[]
    for i in row:
        row1+=[int(i)]
    return row1
for i in range(m):
    row=input("Enter the elements of row " + str(i+1) + ": ").split()
    row1=int_list(row)
    for j in row1:
        main_list+=[j]
main_list.sort()

index1=0
matrix=[]
for i in range(m):
    roww=[]
    for j in range(n):
        roww.append(main_list[index1])
        index1+=1
    matrix.append(roww)

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
        

    