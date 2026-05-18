"""
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
"""
vehicle = input("Enter vehicle number: ")

if len(vehicle) != 10:
    print("Invalid Vehicle Number")

elif not vehicle[0:2].isalpha():
    print("Invalid Vehicle Number")

elif not vehicle[2:4].isdigit():
    print("Invalid Vehicle Number")

else:
    print("Valid Vehicle Number")
