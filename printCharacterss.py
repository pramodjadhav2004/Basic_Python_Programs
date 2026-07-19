# This program takes a number of Unicode values as input from the user and prints the corresponding characters.
num=int(input("Enter the number of Unicode values you want to input: "))
word=""
for i in range(num):
    n=int(input())
    char=chr(n)
    word=word+char
print(word)