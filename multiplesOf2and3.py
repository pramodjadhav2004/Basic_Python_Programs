num = int(input("Enter the number: "))
set_a = set()
set_b = set()
for i in range(1,num+1):
   set_a.add(i*2)
   set_b.add(i*3)
diff = list(set_a - set_b)
symm = list(set_a ^ set_b)
diff.sort()
symm.sort()
print(diff)
print(symm)

   
