string = input("Enter a string: ")
alpha = ""
is_digit = ""
for i in string:
    if i.isalpha():
        alpha += str(i)
    elif i.isdigit():
        is_digit += str(i)
print(alpha+is_digit)