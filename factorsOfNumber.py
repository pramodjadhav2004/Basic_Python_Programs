"""
    Calculates all factors of a given number and returns them as a space-separated string.
    
    Args:
        number (int): The integer for which factors are to be found.
        
    Returns:
        str: A string containing all factors separated by spaces.
    """
def factors_of_n(number):
    factor=""
    for i in range(1,number+1):
        if number%i==0:
            factor+=str(i)+" "
    return factor

number = int(input("Enter a number to find its factors: "))
result = factors_of_n(number)
print(result)