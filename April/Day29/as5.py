"""


=====================================================================5

5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
===


"""

n=int(input("Input:"))
a=1
for i in range(1,n+1):
    if a>=i:
        a=i
        print(a)
        print("Stable Number")
    break
else:
    print("Unstable Number")

