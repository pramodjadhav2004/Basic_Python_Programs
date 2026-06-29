string = input("Enter a string: ").split()
n = int(input("Enter the length of words to remove: "))
result = ""
for i in string:
    if len(i) != n:
        result += str(i)+" "
print(result)