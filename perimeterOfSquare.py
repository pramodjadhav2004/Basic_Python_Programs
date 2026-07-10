#to find the perimeter of a square using function
def perimeter_of_square(arg_1):
    perimeter = arg_1 + arg_1 + arg_1 +arg_1
    return (perimeter)

side = int(input("Enter the side of the square: "))
result = perimeter_of_square(side)
print(result)