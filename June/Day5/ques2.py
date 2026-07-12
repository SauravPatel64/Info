
"""
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
"""


from collections import namedtuple

student = namedtuple("Student",["roll_no","name","course","markks"])

n =int(input("Enter no of Student : "))

for i in  range(n):
    roll = int(input("Enter Student Roll_No :- "))
    name = input("Enter Student Name : ")
    course = input("Enter course : ")
































# from collections import namedtuple
# student=namedtuple("student",["roll_no","name","course","marks"])
# n=int(input("enter no of stu"))

# stu=[]
# for i in range(n):
#     rno=int(input("enter your roll no: "))
#     n=input("enter your name ")
#     c=input("enter your course name: ")
#     m=float(input("enter your marks: "))
#     stu.append(student(rno,n,c,m))

# #display all rows
# for i in stu:
#     for j in i:
#         print(j,end=" ")
#     print()

# #highest
# print()
# print("topper: ")
# hs=0
# hsi=0
# for i in range(len(stu)):
#     a=stu[i][3]
#     if a>hs:
#         hs=a
#         hsi=i
# for j in range(len(stu[hsi])):
#     print(stu[hsi][j],end=" ")
# print()
# #above 80
# c=0
# for i in range(len(stu)):
#     a=stu[i][3]
#     if a>80:
#         c=c+1
# print("count above 80",c)

# #avarage
# sum=0
# for i in range(len(stu)):
#     a=stu[i][3]
#     sum=sum+a
# print("avarage marks",sum//len(stu))

# #in same course
# ec=input("enter course")
# for i in range(len(stu)):
#     a=stu[i][2]
#     if a==ec:
#         for j in range(len(stu[i])):
#             print(stu[i][j],end=" ")
#         print()