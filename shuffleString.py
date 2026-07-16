"""
    Constructs a new string by picking characters from the original string 
    based on a provided space-separated list of indices.
    
    Args:
        string (str): The original string to pick characters from.
        indices_string (str): A space-separated string of integer indices.
        
    Returns:
        str: The newly constructed shuffled string.
    """
def shuffle_string(string, indexes_list):
    result = ""
    index_string = indexes_list.split()
    string_str = string
    for i in index_string:
        ans = int(i)
        result += string_str[ans]
    return (result)
        
string = input("Enter a string to shuffle: ")
indices_list = input("Enter the indices to shuffle (space-separated): ")

result = shuffle_string(string,indexes_list = indices_list)
print(result)