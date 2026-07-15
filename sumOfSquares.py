#to calculate the sum of squares of numbers from m to n
def sum_of_squares_m_to_n(m, n):
    sum=0
    for i in range(m,n+1):
        sum+=i*i
    print(sum)

m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
sum_of_squares_m_to_n(m, n)
