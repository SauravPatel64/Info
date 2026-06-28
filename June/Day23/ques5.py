"""  
5.
 Hospital Record System (Search Digit)


A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264

Enter Digit:
7
Output
Digit Found
"""
n = int(input("Enter Patient ID: "))
D = int(input("Enterr Digit: "))

def digitCheker(n):
    if str(D) in str(n):
        return "Digit Found"
    return "Not Found"

print(digitCheker(n))