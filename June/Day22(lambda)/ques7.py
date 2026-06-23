""" 
Assignment 3: Security PIN Verification (Palindrome Number)

A bank allows customers to choose a special PIN. For promotional purposes, the bank rewards customers whose PIN is a palindrome (reads the same from left to right and right to left).

As a software developer, write a recursive program to verify whether the entered PIN is a palindrome.

Task

Write a recursive function to reverse the given number and determine whether it is a palindrome.

Input 1
Enter PIN:
1221
Output 1
Palindrome Number
Input 2
Enter PIN:
1234
Output 2
Not a Palindrome Number
"""


user_pin = int(input("Enter PIN:\n"))


def reverse_number(n, current_reverse=0):
    if n == 0:
        return current_reverse

    next_reverse = (current_reverse * 10) + (n % 10)


    return reverse_number(n // 10, next_reverse)


print("Output")

if user_pin == reverse_number(user_pin):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
