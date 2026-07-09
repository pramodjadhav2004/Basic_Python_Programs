# Prints a sequence of integers from 1 up to the user's input value.

def print_numbers(number):
    for i in range(1, number + 1):
        print(i)
        
number = int(input("Enter a number: "))
print_numbers(number)