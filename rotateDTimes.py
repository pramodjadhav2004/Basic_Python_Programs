def int_iteration(L):
    num_list = []
    for i in L:
        num = int(i)
        num_list.append(num)
    return num_list

int_list = input("Enter a list of numbers separated by spaces: ").split()
n = int(input("Enter the number of positions to rotate: "))
result = int_iteration(int_list)
for i in range(n):
    result.append(result[i])
    result.remove(result[i])
print(result)








