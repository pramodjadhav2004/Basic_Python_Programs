# This program takes a string input from the user and a Unicode value, and counts how many times the character corresponding to that Unicode value appears in the string.
s=input("Enter a string: ")
num=input("Enter a Unicode value: ")
count=0
for i in range(len(s)):
    uni=ord(s[i])
    if(uni==int(num)):
        count+=1
print(count)