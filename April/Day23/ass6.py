"""
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to **check whether a number is an Armstrong number using loops**.

Input: 153
Output: Armstrong

"""

n = int(input("Enter the number = "))
real = n
arm = 0
while n > 0:
    last = n%10
    arm += last * last * last
    n = n//10

if real == arm:
    print("Armstrong")
else:
    print(" not Armstrong")


