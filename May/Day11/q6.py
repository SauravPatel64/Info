
"""

6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9

"""

n = int(input("Enter size: "))

for i in range(1, n + 1):

    print("- " * (n - i), end="")

    for j in range(i):
        print(i + j, end=" ")

    print()