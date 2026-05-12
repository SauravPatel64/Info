
"""
15) Zig-Zag Star
    *   *   *
      *   *
    *   *   *

"""


n = int(input("Enter size: "))

for i in range(3):

    for j in range(n):

        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()