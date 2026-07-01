str_num = input("Enter a list of numbers separated by spaces: ").split()
int_list = set()
for i in str_num:
    num = int(i)
    int_list.add(num)
if len(int_list) == 1:
    print("True")
else:
    int_list = list(int_list)
    int_list.sort()
    print(int_list)