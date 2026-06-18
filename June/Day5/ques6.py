
"""
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000
"""


n=int(input("enter no of element "))
pro=[]
for i in range(n):
    pid=int(input("enter id: "))
    pname=input("enter product name")
    price=int(input("Enter price : "))
    pro.append((pid,pname,price))
for i in pro:
    print(i)
print()
#max price
print("highest price")
max=pro[0][2]
h=0
for i in range(len(pro)):
    a=pro[i][2]
    if max<a:
        max=a
        h=i
print(pro[h])
print()
print("chepest price")
min=pro[i][2]
h=0
for i in range(len(pro)):
    a=pro[i][2]
    if min>a:
        min=a
        h=i
print(pro[h])
print()


print("average price")
sum=0
for i in range(len(pro)):
    a=pro[i][2]
    sum=sum+a
print(sum//len(pro))
        

print()
print("price above 50000")
for i in range(len(pro)):
    a=pro[i][2]
    if a>50000:
        print(pro[i])