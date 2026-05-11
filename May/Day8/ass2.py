"""
2)WAP to print Square, Cube and Square Root of all numbers from 1 to N
"""


n = int(input("Enter number = "))


for i in range(1,n+1):
    print(f"The Number is = {i}")
    print()
    print(f"Square of this {i} no. = {i**2}")
    print(f"Cube of this {i} no. = {i**3}")
    print(f"Square Root of this {i} no. = {int(i**(1/2))}")
    print()
    print()
