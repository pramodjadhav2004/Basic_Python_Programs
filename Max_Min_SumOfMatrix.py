def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list

m, n = input("Enter the dimensions of the matrix (m n): ").split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.extend(list_a)
print("Maximum:", max(num_list))
print("Minimum:", min(num_list))
print("Sum:", sum(num_list))

