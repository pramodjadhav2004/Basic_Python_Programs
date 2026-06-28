def replace_old_value_with_new_value(matrix, old_value, new_value):
    new_matrix=[]
    for i in matrix:
        row=[]
        for j in i:
            if j==old_value:
                row.append(new_value)
            else:
                row.append(j)
        new_matrix+=[row]
    return new_matrix


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input("Enter rows and columns: ").split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input("Enter matrix: ").split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

values = input("Enter values to replace(old,new): ").split()
old_value, new_value = convert_string_to_int(values)

new_matrix=replace_old_value_with_new_value(num_list, old_value, new_value)
for i in new_matrix:
    print(i)
