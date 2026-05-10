"""

9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books
====
"""

x=input("Membership active (yes/no):")
y=int(input("Book issued:"))

if x=="yes":
    print("Entry allowed")

if y<3:
    print("Can issue more books")
