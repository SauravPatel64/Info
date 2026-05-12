
"""
13) Number X Pattern
    1   5
     2 4
      3
     2 4
    1   5



"""



n = int(input("Enter size: "))

for i in range(n):

    for j in range(n):

        if i == j:
            print(i + 1, end="")

        elif j == n - i - 1:
            print(n - i, end="")

        else:
            print(" ", end="")

    print()
