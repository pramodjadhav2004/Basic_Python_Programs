num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
sub_set = input("Enter a list of numbers separated by spaces: ").split()
no_list=set()
for i in sub_set:
    num = int(i)
    no_list.add(num)
if num_set.issuperset(no_list):
    print("Superset")
elif num_set.issubset(no_list):
    print("Subset")
elif num_set.isdisjoint(no_list):
    print("Disjoint Set")
    
