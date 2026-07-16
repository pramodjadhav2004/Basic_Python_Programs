"""
    Finds and returns the first uppercase letter in a given string.
    
    Args:
        string (str): The string to search through.
        
    Returns:
        str or None: The first uppercase character found, or None if no uppercase letters exist.
    """
def get_first_upper_letter(string):
   for i in string:
       if i.isupper():
           ans = i
           break
   return (ans)

string = input("Enter a string to find the first uppercase letter: ")
upper_case_character = get_first_upper_letter(string)
print(upper_case_character)