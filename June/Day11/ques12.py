
"""
12.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza
"""


orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

d={}

for i in orders:
    c=0
    for j in orders:
        if i==j:
            c=c+1
    d[i]=c
l=list(d.values())
max=l[0]
for i in l:
    if max<i:
        max=i
for k,v in d.items():
    print(k,":",v)
for k,v in d.items():
    if v==max:
        print("most ordered: ",k)


"""
"""
for i in orders:
    d[i]=d.get(i,0)+1
l=list(d.values())
max=l[0]
for i in l:
    if max<i:
        max=i
for k,v in d.items():
    print(k,":",v)
for k,v in d.items():
    if v==max:
        print("most ordered: ",k)
    """