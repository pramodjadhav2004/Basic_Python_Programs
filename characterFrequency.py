string = input("Enter a string to find the frequency of each character: ")
L=[]
for i in string:
    L.append(i.lower())
    set_a = set(L)
    set_a.discard(" ")
sorted_set = sorted(set_a)
for i in sorted_set:
    print(i+": "+str(L.count(i)))