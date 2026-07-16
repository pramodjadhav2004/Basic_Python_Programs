"""
    Finds and prints all prime numbers up to, but not including, 'n'.
    
    Args:
        n (int): The upper limit (exclusive) for generating prime numbers.
    """
def is_prime(n):
    ans = ""
    if n==2:
        print(n)
    for i in range(2,n):
        count = 0
        for j in range(2,i):
            if i % j == 0:
                count = 1
        if count == 0:
            ans+=str(i)+" "
    print(ans)
       
        

n = int(input("Enter a number to find all prime numbers up to that number: "))