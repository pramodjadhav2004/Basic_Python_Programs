#to count the number of vowels in a word using function
def count_the_vowels(word):
    count = 0
    word = word.lower()
    for i in word:
        if i == ("a") or i==("e") or i==("i") or i== ("o") or i==("u"):
            count += 1
    print(count)

word = input("Enter a word: ")
count_the_vowels(word)