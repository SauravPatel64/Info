
"""
12) Hollow Diamond Numbers
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1


"""
n = int(input("Enter size: "))

for i in range(1, n + 1):

    print(" " * (n - i), end="")

    if i == 1:
        print(i)

    else:
        print(str(i) + " " * (2 * i - 3) + str(i))

for i in range(n - 1, 0, -1):

    print(" " * (n - i), end="")

    if i == 1:
        print(i)

    else:
        print(str(i) + " " * (2 * i - 3) + str(i))
