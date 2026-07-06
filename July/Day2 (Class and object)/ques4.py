"""  
Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage	Grade
90 and above	A
75 to 89	B
60 to 74	C
Below 60	D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B

"""


class Student:
    def  __init__(self, roll_number, student_name,marks1,marks2,marks3):
        self.roll_number = roll_number
        self.student_name = student_name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

        print(f"Roll Number      : {self.roll_number}")
        print(f"Student Name     : {self.student_name}")
        total = self.marks1 + self.marks2 + self.marks3
        print(f"Total Marks      : {total}")
        p = total/3
        print(f"Percentage       : {'A' if p>=90 else "B" if p>75 or p<=89 else "C"}")
        

r = int(input("Enter Roll Number : "))
n = input("Enter Student Name : ")
m1 = int(input("Enter Marks in Subject 1 : "))
m2 = int(input("Enter Marks in Subject 2 : "))
m3 = int(input("Enter Marks in Subject 3 : "))

s1 = Student(r,n,m1,m2,m3)