
"""
=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3

"""
from collections import namedtuple
n=int(input("enter user "))
user=namedtuple("user",["order_id","customer_name","product_name","amount"])
sales=[]
for i in range(n):
    oid=int(input("Enter usre id "))
    n=input("Enter usre name ")
    p=input("Enter product name ")
    am=int(input("Enter mount "))
    sales.append(user(oid,n,p,am))
#display
for i in sales:
    for j in i:
        print(j,end=" ")
    print()
#highest
max=0
h=i
for i in range(len(sales)):
    a=sales[i][3]
    if max<a:
        max=a
        h=i
print("highest order value")
for j in range(len(sales[h])):
    print(sales[h][j],end=" ")
print()

#order above than 10000
print("order above 10000")
c=0
for i in range(len(sales)):
    a=sales[i][3]
    if a>10000:
        c=c+1
print(c)