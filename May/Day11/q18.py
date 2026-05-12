"""

18) Binary Floyd Triangle
    1
    0 1
    1 0 1
    0 1 0 1

"""

n = int(input("Enter size: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):

        print((i + j) % 2, end=" ")

    print()
