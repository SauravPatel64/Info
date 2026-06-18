"""
2.
Student Pass List Generator (Using List Comprehension)

A school stores student marks in a list. Generate a new list containing only the marks of students who have passed (marks ≥ 40).

Requirements
Read N and marks from user
Use List Comprehension
Create Pass List
Display Pass Count
Test Case

Input:

[25, 40, 55, 78, 30, 90]

Output:

Pass List = [40, 55, 78, 90]
Pass Count = 4
"""
"""
n=list(map(int,input("enter your marks").split()))
print(n)
c=0
b=[ i for i in n  if i>=40]

print("pass list",b)
c=0
for j in b:
    c=c+1
print("pass count",c)

"""
#                   orr
"""
n=list(map(int,input("enter your marks").split()))
print(n)
c=0
b=[ i for i in n  if i>=40]

print("pass list",b)
print("pass count",len(b))

"""

