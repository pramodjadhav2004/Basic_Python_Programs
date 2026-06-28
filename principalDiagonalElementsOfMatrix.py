def get_principal_diagonal_elements(matrix, m, n):
    principal_diagonal=[]
    for i in range(m):
        for j in range(n):
            if i==j:
                principal_diagonal+=[matrix[i][j]]
    print(principal_diagonal)

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
    list_a = input("Enter Matrix: ").split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

get_principal_diagonal_elements(num_list, m, n)
