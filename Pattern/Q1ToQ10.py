# =========================
# Q1
# =========================

"""
*****
*****
*****
*****
*****
"""

"""
n = int(input("Enter Number = "))

for i in range(n):
    print("*" * n)
"""


# =========================
# Q2
# =========================

"""
*
*
*
*
*
"""

"""
n = int(input("Enter Number = "))

for i in range(n):
    print("*")
"""


# =========================
# Q3
# =========================

"""
*
 *
  *
   *
    *
"""

"""
n = int(input("Enter Number = "))

for i in range(n):
    print(" " * i + "*")
"""


# =========================
# Q4
# =========================

"""
*****
*****
*****
*****
*****
"""

"""
n = int(input("Enter Number = "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
"""


# =========================
# Q5
# =========================

"""
12345
12345
12345
12345
12345
"""

"""
n = int(input("Enter Number = "))

for i in range(n):

    for j in range(1, n + 1):
        print(j, end="")

    print()
"""


# =========================
# Q6
# =========================

"""
11111
22222
33333
44444
55555
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):
    print(str(i) * n)
"""


# =========================
# Q7
# =========================

"""
1
00
111
0000
11111
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    print(str(i % 2) * i)
"""


# =========================
# Q8
# =========================

"""
*
**
***
****
*****
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    print("*" * i)
"""


# =========================
# Q9
# =========================

"""
1
12
123
1234
12345
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end="")

    print()
"""


# =========================
# Q10
# =========================

"""
1
22
333
4444
55555
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    print(str(i) * i)
"""


# =========================
# Q11
# =========================

"""
A
AB
ABC
ABCD
ABCDE
"""

"""
n = int(input("Enter Number = "))

for i in range(n):

    for j in range(i + 1):
        print(chr(65 + j), end="")

    print()
"""


# =========================
# Q12
# =========================

"""
a
ab
abc
abcd
abcde
"""

"""
n = int(input("Enter Number = "))

for i in range(n):

    for j in range(i + 1):
        print(chr(97 + j), end="")

    print()
"""


# =========================
# Q13
# =========================

"""
1
01
101
0101
10101
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    for j in range(i):
        print((i + j) % 2, end="")

    print()
"""


# =========================
# Q14
# =========================

"""
1
23
456
78910
"""

"""
n = int(input("Enter Number = "))

num = 1

for i in range(1, n + 1):

    for j in range(i):

        print(num, end="")
        num += 1

    print()
"""


# =========================
# Q15
# =========================

"""
A
BB
CCC
DDDD
EEEEE
"""

"""
n = int(input("Enter Number = "))

for i in range(n):

    print(chr(65 + i) * (i + 1))
"""


# =========================
# Q16
# =========================

"""
a
bc
def
ghij
klmno
"""

"""
n = int(input("Enter Number = "))

ch = 97

for i in range(1, n + 1):

    for j in range(i):

        print(chr(ch), end="")
        ch += 1

    print()
"""


# =========================
# Q17
# =========================

"""
*
##
***
####
*****
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    if i % 2 == 0:
        print("#" * i)

    else:
        print("*" * i)
"""


# =========================
# Q18
# =========================

"""
1
10
101
1010
10101
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    for j in range(i):

        if j % 2 == 0:
            print("1", end="")

        else:
            print("0", end="")

    print()
"""


# =========================
# Q19
# =========================

"""
*
* *
*   *
*     *
* * * * *
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if j == 1 or j == i or i == n:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
"""


# =========================
# Q20
# =========================

"""
1
12
1 3
1  4
12345
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    if i == 1:
        print("1")

    elif i == n:

        for j in range(1, n + 1):
            print(j, end="")

        print()

    else:
        print("1" + " " * (i - 2) + str(i))
"""


# =========================
# Q21
# =========================

"""
1
22
3 3
4 4
55555
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    if i == n:
        print(str(i) * i)

    elif i <= 2:
        print(str(i) * i)

    else:
        print(str(i) + " " * (i - 2) + str(i))
"""


# =========================
# Q22
# =========================

"""
A
AB
A C
A  D
ABCDE
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    if i == 1:
        print("A")

    elif i == n:

        for j in range(i):
            print(chr(65 + j), end="")

        print()

    else:
        print("A" + " " * (i - 2) + chr(64 + i))
"""


# =========================
# Q23
# =========================

"""
a
bc
d f
g  j
klmno
"""

"""
n = int(input("Enter Number = "))

ch = 97

for i in range(1, n + 1):

    if i == 1:
        print(chr(ch))
        ch += 1

    elif i == n:

        for j in range(i):
            print(chr(ch), end="")
            ch += 1

        print()

    else:

        first = chr(ch)
        ch += i - 1

        last = chr(ch)
        ch += 1

        print(first + " " * (i - 2) + last)
"""


# =========================
# Q24
# =========================

"""
5
54
543
5432
54321
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    for j in range(n, n - i, -1):

        print(j, end="")

    print()
"""


# =========================
# Q25
# =========================

"""
*
*#
*#*
*#@*
* @ @ *
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if j == 1 or j == i:
            print("*", end="")

        elif j % 2 == 0:
            print("#", end="")

        else:
            print("@", end="")

    print()
"""


# =========================
# Q26
# =========================

"""
1
10
1 1
1  0
10101
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    if i == 1:
        print("1")

    elif i == n:

        for j in range(i):

            if j % 2 == 0:
                print("1", end="")

            else:
                print("0", end="")

        print()

    else:
        print("1" + " " * (i - 2) + str(i % 2))
"""


# =========================
# Q27
# =========================

"""
1
123
12345
1234567
123456789
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    for j in range(1, 2 * i):

        print(j, end="")

    print()
"""


# =========================
# Q28
# =========================

"""
1
222
33333
4444444
555555555
"""

"""
n = int(input("Enter Number = "))

for i in range(1, n + 1):

    print(str(i) * (2 * i - 1))
"""


# =========================
# Q29
# =========================

"""
*****
****
***
**
*
"""

"""
n = int(input("Enter Number = "))

for i in range(n, 0, -1):

    print("*" * i)
"""


# =========================
# Q30
# =========================

"""
12345
1234
123
12
1
"""

"""
n = int(input("Enter Number = "))

for i in range(n, 0, -1):

    for j in range(1, i + 1):

        print(j, end="")

    print()
"""