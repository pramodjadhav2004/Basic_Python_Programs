# Evaluates the user's input amount and prints the corresponding discount tier (5%, 10%, or 20%).

def get_discount(amount):
    if amount < 500:
        print("5%")
    elif amount >= 500 and amount < 2500:
        print("10%")
    else:
        print("20%")

amount = int(input("Enter the amount: "))
discount = get_discount(amount)