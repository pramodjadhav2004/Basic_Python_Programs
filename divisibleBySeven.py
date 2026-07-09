# Checks if the user's integer input is divisible by 7 and prints True or False.

def divisible_by_seven(arg_1):
    if arg_1 % 7 == 0:
        print("True")
    else:
        print("False")

n = int(input("Enter a number: "))
divisible_by_seven(n)