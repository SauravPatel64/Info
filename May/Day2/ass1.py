"""
1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.
For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14 
Unstable Number
"""


temp = int(input("Input = "))

sum = 0
small = 99
digit = 0
prod = 1
n=0

while temp>0:
    last = temp%10
    n = n*10 + last
    temp = temp//10


first = n %10
n = n // 10


while n >0:
    digit += 1
    second = n%10
    prod = first * second
    first = second
    n = n//10
    sum = sum + prod
    print(prod) 
    if small > prod:
        small = prod
    


else:
    print(f"Sum = {sum}")
    print(f"Smallest = {small}")
    
    if sum % digit == 0:
        print("Stable Number")
    else:
        print("Unstable Number")












