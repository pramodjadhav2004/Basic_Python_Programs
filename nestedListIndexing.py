num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
flag=0
n = int(input("Enter number: "))
for i in range (len(num_list)):
     for j in range (len(num_list[i])):
         if num_list[i][j] == n:
             print(str(i)+" "+str(j))
             flag=1
if flag==0:
    print("Given number is not in the list.")
         

        