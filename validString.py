#to check if a string is valid or not using function
def valid_string(string):
    if  string[0].isdigit(): 
        result = "Valid String"
    elif  (len(string) >= 6):
        result = "Valid String"
    else:
        result ="Invalid String"
    return(result)
        
string = input("Enter a string: ")
result = valid_string(string)
print(result)