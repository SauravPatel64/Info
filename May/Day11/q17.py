"""
17) Hollow Hourglass
    * * * * *
      *     *
        * *
          *
        * *
      *     *
    * * * * *

"""

n = int(input("Enter size: "))

for i in range(n):

    print(" " * (2 * i), end="")

    for j in range(2 * (n - i) - 1):

        if i == 0 or j == 0 or j == 2 * (n - i) - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range(1, n):

    print(" " * (2 * (n - i - 1)), end="")

    for j in range(2 * (i + 1) - 1):

        if i == n - 1 or j == 0 or j == 2 * (i + 1) - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

