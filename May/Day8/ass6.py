"""
6)
a
ab
abc
abcd
abcde
"""


n = int(input("Enter number = "))

for i in range(1,n+1):
    for j in range(97,97+i):
        print(chr(j),end="")
    print()
        