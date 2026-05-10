"""

5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
====
"""

ad=input("Enter username:")
p=(input("Enter password:"))

if ad=="admin":
    print("Valid user")
if len(p)>=8:
    print("Strong password")
