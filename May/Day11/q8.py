
"""

8) Border Number Pattern
    1 2 3 4 5
    2       5
    3       5
    4       5
    5 5 5 5 5

"""
n = int(input("Enter size: "))

for i in range(1, n + 1):

    for j in range(1, n + 1):

        if i == 1:
            print(j, end=" ")

        elif i == n:
            print(n, end=" ")

        elif j == 1:
            print(i, end=" ")

        elif j == n:
            print(n, end=" ")

        else:
            print(" ", end=" ")

    print()