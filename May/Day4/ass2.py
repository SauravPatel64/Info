"""
2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number+
"""

num =input("Input : ")


len = len(num)
rev = 0
halfLen = len//2
left = int(num)
leftNum = left//10**halfLen
leftSum = 0
while leftNum>0:
    last = leftNum%10
    leftSum = leftSum*10 + last
    leftNum = leftNum//10

n = int(num)

while n>0:
    last =n%10
    rev = rev*10 + last
    n = n//10

rightNum  = rev//10**halfLen
rightSum = 0

while rightNum >0:
    last = rightNum%10
    rightSum = rightSum*10 + last
    rightNum = rightNum//10

if leftSum == rightSum:
    print("Balanced Number")
else:
    print("Unbalanced Number")



