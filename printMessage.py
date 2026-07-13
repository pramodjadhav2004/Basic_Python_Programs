#to print a message using function and parameters
def message(arg_1, arg_2):
    print(arg_1+" is a "+arg_2+" years old.")

name = input()
age = int(input())
message(name,age)