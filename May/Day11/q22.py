"""

22) Inverted Hollow Pyramid
    *********
     *     *
      *   *
       * *
        *


"""

n = int(input("Enter size: "))

for i in range(n, 0, -1):

    print(" " * (n - i), end="")

    for j in range(2 * i - 1):

        if i == n or j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()