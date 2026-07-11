"""
    Calculates the final bill amount by applying tiered discounts:
    - 5% off for amounts under 500
    - 10% off for amounts between 500 and 2499
    - 20% off for amounts 2500 and above
    """
def calculate_bill(amount):
    discount=0
    if amount<500:
        discount=(5/100)*amount
    elif amount>=500 and amount<2500:
        discount=(10/100)*amount
    elif amount>=2500:
        discount=(20/100)*amount
    print(amount-round(discount,3))


amount = int(input("Enter the amount: "))
calculate_bill(amount)