"""
    Evaluates a number based on standard FizzBuzz rules:
    - Prints 'FizzBuzz' if divisible by both 3 and 5.
    - Prints 'Fizz' if divisible only by 3.
    - Prints 'Buzz' if divisible only by 5.
    - Prints the number itself if none of the above apply.
    """
def fizz_buzz(number):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)


number = int(input("Enter a number: "))
fizz_buzz(number)