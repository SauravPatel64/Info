"""
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
"""

password = input("Enter password: ")

if len(password) < 8 or len(password) > 15:
    print("Not Secure Password")

elif not password[0].isupper():
    print("Not Secure Password")

elif not password[-1].isdigit():
    print("Not Secure Password")

elif " " in password:
    print("Not Secure Password")

else:
    digit_count = 0
    special_count = 0
    special_chars = "@#$%&*"

    for ch in password:
        if ch.isdigit():
            digit_count += 1
        if ch in special_chars:
            special_count += 1

    if digit_count >= 2 and special_count >= 1:
        print("Secure Password")
    else:
        print("Not Secure Password")