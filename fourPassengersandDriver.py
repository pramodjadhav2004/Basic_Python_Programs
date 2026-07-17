"""
Car Allocation Calculator

This script determines the minimum number of cars required to transport 
a specific number of people, assuming a fixed capacity of 5 people per car.
It utilizes ceiling division to ensure that even a single extra person 
will correctly allocate an additional car.
"""
import math
def number_of_cars_needed(no_of_people):
    ans=no_of_people/5
    ans=int(math.ceil(ans))
    print(ans)


no_of_people = int(input("Enter the number of people: "))
number_of_cars_needed(no_of_people)
