#to count the number of uppercase letters in a word using function
def count_of_uppercase(word):
    count = 0
    for i in word:
        if i.isupper():
           count += 1 
    return (count)
    
word = input("Enter a word: ")
result = count_of_uppercase(word)
print(result)