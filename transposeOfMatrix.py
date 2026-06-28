def get_transpose_of_matrix(matrix, m, n):
    for i in range(n):
        transpose=[]
        for j in range(m):
            transpose.append(matrix[j][i])
        print(transpose)
            

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

get_transpose_of_matrix(num_list, m, n)
