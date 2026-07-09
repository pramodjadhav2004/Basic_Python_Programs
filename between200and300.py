# Evaluates if the user's input is between 200 and 500 (exclusive) and prints Yes or No.

def is_between_200_and_500(number):
    if 200 < number < 500:
        ans = "Yes"
    else:
        ans = "No"
    return (ans)
    
number = int(input("Enter a number: "))
num_call = is_between_200_and_500(number)
print(num_call)