# Iterates from 0 to the user's input, printing whether each number is EVEN or ODD.

def show_numbers(number):
    for i in range(number+1):
        if i % 2 == 0:
            print(str(i)+" EVEN")
        else:
            print(str(i)+ " ODD")
        
number = int(input("Enter a number: "))
show_numbers(number)