"""
Given a string, write a program to print a secret message that replaces
characters with numbers 'a' with 1, 'b' with 2, ..., 'z' with 26 where characters
are separated by '-'.

Note: You need to replace both uppercase and lowercase characters. You can
ignore replacing all characters that are not letters.
"""
str1=input("Enter the message to encode: ").split()
final_str=""
for i in str1:
    final=[]
    for j in i:
        if j.lower().isalpha():
            index=ord(j.upper())-64
            final.append(str(index))
    final_str+="-".join(final)+" "
print(final_str)