num_string = (input("Enter elements separated by space: ")).split()
new_list=[]
for i in num_string:
    num = int(i)
    new_list.append(num)
new_set = set(new_list)
new_list_1 =list(new_set)
new_list_1.sort()
print(new_list_1)
    
