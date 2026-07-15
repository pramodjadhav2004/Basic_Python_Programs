#This program checks if any of the three numbers entered by the user is divisible by 9.
def check_divisible_by_9(first_number, second_number, third_number):
    if (first_number%9==0 or second_number%9==0 or third_number%9==0):
        return True
    else:
        return False
    

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

result = check_divisible_by_9(first_number, second_number, third_number)

print(result)