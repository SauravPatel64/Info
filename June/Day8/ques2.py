

"""
2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.
"""


python=set()
java=set()
p=0

j=0
while True:
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")

    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            python=set(input("enter email ").split())
            p=1
        case 2:
            java=set(input("enter email ").split())
            j=1
        case 3:
            if p==0:
                print("pls enter element in pyhone")
            else:
                print(python)
        case 4:
            if j==0:
                print("pls enter element in java")
            else:
                print(java)
        case 5:
            if j==0 and p==0:
                print("pls enter email first")
            else:
                print(python&java)
        case 6:
            if p==0:
                print("pls enroll first")
            else:
                print(python-java)
        case 7:
            if java==0:
                print("pls enroll first")
            else:
                print(java-python)
        case 8:
            if p==0:
                print("pls enter first")
            else:
                n=input("enter your name")
                if n in python:
                    print("student in python")
                else:
                    print("not found")
        case 9:
            print(python|java)
        case 10:
            print("exit")
            break