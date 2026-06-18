
"""
5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers. 
Your task is to create an array of alternate positive and negative numbers 
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input: 
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input: 
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
"""


n1=int(input("enter no1 "))
a=[]
for i in range(n1):
    x=int(input("enter element: "))
    a.append(x)
print(a)
p=[]
n=[]
for i in a:
    if i>=0:
        p.append(i)
    else:
        n.append(i)
print(p)
print(n)
res=[]
i=0
j=0
while i<len(p) or j<len(p):
    res.append(p[i])
    res.append(n[j])
    i=i+1
    j=j+1
print(res)







