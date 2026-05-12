"""

29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4
"""

n = int(input("Enter size: "))

for i in range(1, n + 1):

    for j in range(1, n + 1):

        if i == j:
            print(i, end=" ")
        else:
            print("-", end=" ")

    print()