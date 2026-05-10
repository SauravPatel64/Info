"""
5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome

"""
n = int(input("Enter the number = "))
realNum = n
rev = 0
while n>0:
    last = n%10
    rev = rev * 10 + last
    n = n//10
if realNum == rev:
    print("Palindrome")
else:
    print("not a palindrome")


