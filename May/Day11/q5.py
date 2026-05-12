"""
5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1

"""

n = int(input("Enter size: "))

for i in range(n):
    for j in range(1, n - i + 1):
        print(j, end="")

    print("*" * (2 * i), end="")

    for j in range(n - i, 0, -1):
        print(j, end="")

    print()