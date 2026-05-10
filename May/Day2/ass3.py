"""
3.
Zero Detection & Early Termination System

A financial system scans transaction IDs digit by digit. If a digit '0' is found, the system immediately stops processing further digits for security reasons.

Write a program to:

Traverse each digit of the number from right to left
Display each digit processed before encountering 0
Stop the loop immediately when 0 is found using break
Count how many digits were processed before termination
If no zero is found, print No Zero Found

Use loops and break wherever required.

Input:
572049

Output:
Digits Processed: 9 4
Count = 2
Zero Found - Process Stopped

Input:
56789

Output:
Digits Processed: 9 8 7 6 5
Count = 5
No Zero Found
"""

n = int(input("Input = "))
i = 0

print("Digits Processed = ")
while n>0:
    last = n%10
    if last != 0:
        i = i+1
        print(last)
        n = n//10
    else:
        print(f"Count = {i}")
        print("Zero Found - Process Stopped")
        break

else:
    print(f"Count = {i}")
    print("No Zero Found ")























