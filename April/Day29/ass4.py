"""

4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
===

"""

n=int(input("Input:"))

for i in range(1,n+1):
    a=n%10
    if a==i:
        print("Not Unique Code")
    n=n//10
else:
    print("Valid Unique Code")
