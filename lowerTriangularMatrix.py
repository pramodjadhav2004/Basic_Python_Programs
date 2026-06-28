def print_lower_triangle(matrix,m,n):
        L = []
        for j in range(m):
            L = (matrix[j][:j+1])
            print(L)
             

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

print_lower_triangle(num_list,m,n)
