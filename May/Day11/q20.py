"""

20) Continuous Diamond Numbers
           1
          2 3
         4 5 6
        7 8 9 10
         4 5 6
          2 3
           1

"""

n = int(input("Enter size: "))

num = 1

for i in range(1, n + 1):

    print(" " * (n - i), end="")

    temp = num

    for j in range(i):
        print(temp, end=" ")
        temp += 1

    num = temp
    print()

for i in range(n - 1, 0, -1):

    print(" " * (n - i), end="")

    temp = num - i

    for j in range(i):
        print(temp, end=" ")
        temp += 1

    print()

