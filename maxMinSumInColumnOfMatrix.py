def get_transpose_of_matrix(matrix, m, n):
    transpose=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(matrix[j][i])
        transpose.append(row)
    return transpose


def print_max_min_sum_for_row_wise(num_list):
    maxL=[]
    minL=[]
    sumL=[]
    for i in num_list:
        maxL+=[max(i)]
        minL+=[min(i)]
        sumL+=[sum(i)]
    print(maxL)
    print(minL)
    print(sumL)


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


transpose=get_transpose_of_matrix(num_list, m, n)
print_max_min_sum_for_row_wise(transpose)
