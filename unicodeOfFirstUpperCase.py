# This program takes a string input from the user and prints the Unicode value of the first uppercase letter in the string.
s=input("Enter a string: ")
for i in range(len(s)):
    uni=ord(s[i])
    if(uni>=65 and uni<=90):
        print(uni)
        break