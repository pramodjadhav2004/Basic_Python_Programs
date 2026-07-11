# Iterates through the input string to check for numeric characters, 
# returning "Valid" only if there is an unbroken sequence of exactly 4 or 6 digits.
def validate_atm_pin_code(pin):
    count = 0
    for i in pin:
        if i.isdigit():
            count+= 1
        else:
            count = 0
    if count == 4:
       print("Valid PIN Code")
    elif count == 6:
       print("Valid PIN Code")
    else :
       print("Invalid PIN Code")
    
pin = input("Enter your ATM PIN code: ")
validate_atm_pin_code(pin)