strr1 = input("Enter the first list of numbers separated by spaces: ").split()
strr2 = input("Enter the second list of numbers separated by spaces: ").split()
strr3 = input("Enter the third list of numbers separated by spaces: ").split()

def iteration_num(L):
    sets = set()
    for i in L:
        num = int(i)
        sets.add(num)
    return sets

set_1 = iteration_num(strr1)
set_2 = iteration_num(strr2)
set_3 = iteration_num(strr3)


unique_ans = ((set_1 & set_2) & set_3)
print(list(unique_ans))
    
    
    
    
    
    
    
    
    
