#This program checks if both numbers entered by the user are greater than 100 and if the first number is less than the second number.
def compare_numbers(first_number, second_number):
    if (first_number>100 and second_number>100 and first_number<second_number):
        return True
    else:
        return False
    

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

is_true = compare_numbers(first_number, second_number)

print(is_true)