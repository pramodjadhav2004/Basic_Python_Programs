num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
strr = input("Enter elements to remove separated by space: ").split()
num_list = []
for i in strr:
    num = int(i) 
    num_list.append(num)
num_set_1 = set(num_list)
diff = num_set.difference(num_set_1)
diff_list = list(diff)
diff_list.sort()
print(diff_list)