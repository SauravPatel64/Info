"""
5.
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number
"""

num = input("Input : ")

n = int(num)
halfLen = len(num)//2

leftDigit = 0
rightDigit = 0
rev = 0

if len(num)%2==0:
    leftDigit = n%(10**halfLen)
    rightDigit  = n//(10**halfLen)
    print(f"First Half = {leftDigit}")
    print(f"Second Half = {rightDigit}")
    sum = leftDigit + rightDigit
    print(f"Sum = {sum}")
    print(f"Square = {sum**2}")
    
    if sum**2 == n:
        print("Tech Number")
    else:
        print("Not a Tech number")

else:
    print("please enter a even digit number")
        
    
       


    



























