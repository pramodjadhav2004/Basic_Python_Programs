#to print the count of uppercase and lowercase letters in a string
def count_of_lowercase_and_uppercase_letters(arg_1):
    count_of_uppercase=0
    count_of_lowercase=0
    for i in arg_1:
        if i.isupper():
            count_of_uppercase+=1 
        elif i.islower():
            count_of_lowercase+=1
    print(count_of_uppercase)
    print(count_of_lowercase)


word = input("Enter a word: ")
count_of_lowercase_and_uppercase_letters(word)