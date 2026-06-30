str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
char=str1[0]
if char in str2 and len(str1)==len(str2):
    index=str2.index(char)
    print(index)
else:
    print("No Match")