
"""

7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5

"""
n = int(input("Enter size: "))

for i in range(1, n + 1):

    for j in range(i):
        print((i * 2) - j, end=" ")

    print("- " * (n - i))