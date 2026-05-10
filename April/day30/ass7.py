"""
7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144
"""

n = int(input("Enter a number = "))

temp = n
revNum = 0

while temp>0:
    last = temp%10
    revNum = revNum*10 + last
    temp = temp // 10

sqRev = revNum**2
sqRevRev = sqRev
sqNum = n**2

reverse = 0
while sqRevRev >0:
    last = sqRevRev%10
    reverse = reverse*10 + last
    sqRevRev = sqRevRev // 10
        

else:
    if sqNum == reverse:
        print("Adam Number")
    else:
        print("Not a Adam Number")
    






















