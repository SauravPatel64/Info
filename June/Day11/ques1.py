"""
1.

=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6
"""


n=int(input("enter no product: "))
d={}
for i in range(n):
    key=input("enter product name: ")
    value=int(input("enter quantity: "))
    d[key]=value
print(d)
print("total quantity",sum(d.values()))