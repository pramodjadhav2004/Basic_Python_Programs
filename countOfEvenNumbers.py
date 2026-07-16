"""
    Counts the number of even integers in a space-separated string of numbers.
    
    Args:
        numbers_string (str): A string containing numbers separated by spaces.
        
    Returns:
        int: The total count of even numbers found in the string.
    """
def get_even_numbers_count(numbers):
    count = 0
    string = numbers.split()
    for i in string:
       ans = int(i)
       if ans % 2 == 0:
           count += 1
    return (count)
        

numbers = input("Enter a list of numbers separated by spaces to count the even numbers: ")
result = get_even_numbers_count(numbers)
print(result)