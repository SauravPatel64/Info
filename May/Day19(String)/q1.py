"""
1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ********9012
"""
num = input("Enter account number: ")

l = len(num)

result = ""
print(l)
print(num[l-4:l])

first  = "*"*(l-4)

result = result + first + str(num[l-4:l])

print(f"Masked Account: {result}")

print("a".upper())