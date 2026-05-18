"""

1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username

"""
email = input("Enter username: ")
flag=1
count = len(email)
if count>=5 or count<=12:
    flag=1
  
first = email[0]

if ((first>='A' and first<="Z") or (first>='a' and first<='z')):
    flag=1
    
for ch in email:
    if ch==" ":
        flag=0
        break
    
    if ((ch>="A" and ch<="Z") or (ch>='a' and ch<='z') or (ch >='0' and ch<='9') or (ch=="_")):
        flag=1
    else:
        flag=0
        break

if flag == 1:
    print("Valid Username")
else:
    print("Invalid User")


    