"""
**8. Count Odd Digits**
A banking system flags IDs with too many odd digits for further verification.
Write a program to **count the number of odd digits in a given number using loops**.

Input: 123456
Output: Odd digits count = 3
"""

n = int(input("Enter the number = "))
count = 0
while n>0:
    last = n%10
    n = n//10
    if last % 2 !=0:
        count += 1

print(f"Odd digits count = {count}")