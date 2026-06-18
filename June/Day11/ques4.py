"""
4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
"""

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
l=list(students.values())
print(l)
max=l[0]
for i in l:
    if i>max:
        max=i
min=l[0]
for i in l:
    if i<min:
        min=i
for k,v in students.items():
    if v==max:
        print("Highest Marks:",k ,v)
    if v==min:
        print("lowest marks:",k,v)


