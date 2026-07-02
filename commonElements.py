set_a = input("Enter elements of set A separated by commas: ").split(',')
set_b = input("Enter elements of set B separated by commas: ").split(',')
set_1 = set(set_a)
set_2 = set(set_b)
intersect = list(set_1 & set_2)
listt = []
for i in intersect:
    num = int(i)
    listt.append(num)
listt.sort()
print(listt)