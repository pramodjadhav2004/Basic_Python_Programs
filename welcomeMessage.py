# Prompts the user for a name and prints a personalized welcome message.
def say_wishes(arg_1):
    word = "Welcome "+ arg_1
    print(word)

name = input("Enter your name: ")
say_wishes(name)