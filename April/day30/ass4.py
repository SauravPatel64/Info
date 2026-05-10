"""
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
"""

n = int(input("Input = "))

temp = n
sum = 0
prod = 1

while n>0:
    digit = n%10
    sum += digit
    prod *= digit
    n = n//10

else:
    if sum == prod:
        print("Spy Number")
    else:
        print("Not")
    
