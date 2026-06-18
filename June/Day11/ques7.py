

"""
7.

=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Rav
"""

n=int(input("enter how many stu: "))
d={}
for i in range(n):
    key=input("enter your name: ")
    value=int(input("enter your marks: "))
    d[key]=value
print(d)
for k,v in d.items():
    if v>=50:
        print("pass student",k)








