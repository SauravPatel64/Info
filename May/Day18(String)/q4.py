"""
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
"""

idd = input("Enter Employee ID: ")

first = idd[0:3]
len = len(idd)
f = 0
if len==8 and first=="EMP":
    i=3
    while i<len:
        if idd[i]>='0'and idd[i]<='9':
            f=1
        else:
            f=0
            break
        i = i+1

if f==1:
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")
        