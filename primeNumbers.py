"""
    Checks if a given integer is a prime number.
    
    It determines this by counting the total number of divisors. 
    A number is prime if it has exactly two divisors: 1 and itself.
    
    Args:
        number (int): The integer to be checked.
        
    Returns:
        str: "Prime Number" if the condition is met, "Not a Prime Number" otherwise.
    """
def is_prime(number):
    count = 0
    for i in range(1,number+1):
         if (number % i) == 0:
            count += 1
    if count == 2:
        ans =("Prime Number")
    else:
        ans = ("Not a Prime Number")
    return (ans)

number = int(input("Enter a number to check if it is prime: "))
result = is_prime(number)
print(result)