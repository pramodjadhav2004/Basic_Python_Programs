# This program takes a string input from the user and prints the Unicode values of each character in the string.
s=input("Enter a string: ")
for i in range(len(s)):
    print(ord(s[i]))