#to calculate percentage of a given number using function
def calculate_percentage(number):
    if number < 1000:
        percent = (5/100) * number
        ans=percent
    else:
        percent = (10/100) * number
        ans = percent
    return (ans)

number = int(input("Enter a number: "))
result = calculate_percentage(number)
print(result)