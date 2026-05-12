"""

19) Reverse Number Cross
    5   5
     4 4
      3
     4 4
    5   5

"""

n = int(input("Enter size: "))

for i in range(n):

    for j in range(n):

        if i == j or i + j == n - 1:
            print(n - i, end="")
        else:
            print(" ", end="")

    print()
