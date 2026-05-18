"""
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
"""
code = input("Enter product code: ")

back = code[::-1]

if code==back:
    print("Palindrome Code")
else:
    print("Not a Palindrome Code")