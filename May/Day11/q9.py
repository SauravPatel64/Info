
"""
9) Hollow Diamond Square
    ***********
    ****   ****
    ***     ***
    **       **
    *         *
    *         *
    **       **
    ***     ***
    ****   ****
    ***********

"""

n = int(input("Enter size: "))

for i in range(n):

    for j in range(n - i):
        print("*", end="")

    print(" " * (2 * i), end="")

    for j in range(n - i):
        print("*", end="")

    print()

for i in range(n - 1, -1, -1):

    for j in range(n - i):
        print("*", end="")

    print(" " * (2 * i), end="")

    for j in range(n - i):
        print("*", end="")

    print()
