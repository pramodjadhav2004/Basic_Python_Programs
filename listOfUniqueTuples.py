def int_list(L):
    k =[]
    for i in L:
        k += [int(i)]
    return k
n = int(input("Enter n: "))
L = []
final_list = []
for i in range(n):
    L = (input("Enter tuples: ").split())
    ans = int_list(L)
    set_a = set(ans)
    if len(set_a)==len(ans):
        final_list.append(ans)
print(final_list)
    
    
    
    
    