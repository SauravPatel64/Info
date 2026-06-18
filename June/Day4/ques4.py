"""
4.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C
"""

n1=int(input("enter no1 "))
a=[]
for i in range(n1):
    x=int(input("enter element: "))
    a.append(x)
n2=int(input("enter no1 "))
b=[]
for i in range(n2):
    x=int(input("enter element: "))
    b.append(x)
n3=int(input("enter no1 "))
c=[]
for i in range(n3):
    x=int(input("enter element: "))
    c.append(x)
r=[]
for i in a:
    for j in b:
        for k in c:
            if i==j==k:
                r.append(i)
for i in r:
    
        print(i,end=" ")