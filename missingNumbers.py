strr_no = input("Enter a list of numbers separated by spaces: ").split()
newlist =[]
ans = []
for i in strr_no:
    num = int(i)
    newlist.append(num)
for i in range(1,newlist[-1]+1):
    if i not in newlist:
        ans.append(i)
ans.sort()
print(ans)