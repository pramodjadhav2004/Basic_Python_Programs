n = int(input("Enter the number of sets: "))
main_list = []
def convert_int_list(num):
    int_list = []
    for i in num:
        int_list += [int(i)]
    return int_list

for i in range(n):
    num = input("Enter elements of set {}: ".format(i+1)).split()
    num = convert_int_list(num)
    main_list.append(num)
intersect = []
for i in range(len(main_list)-1):
    intersect = set(main_list[i]) & set(main_list[i+1])
final_list = list(intersect)

if n == 1:
    final_list = main_list[0]
final_list.sort()
print(final_list)
    







    