
"""
1.
STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

*** STUDENT RESULT MANAGEMENT ***

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability
"""

while True:
    print("1. Add Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Find Grade")
    print("5. Display Result")
    print("6. Find Highest Mark")
    print("7. Find Lowest Mark")
    print("8. Exit")
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            def add(name,id,*marks):
                print("name is",name)
                print("id",id)
                for i in range(len(ma)):
                    
                        print("subject",i+1,ma[i])
                    
                        
           
            na=input("enter your name")
            id=int(input("enter your id"))
            ma=[]
            
            for i in range(5):
                x=int(input("enter no of marks"))
                if 0<x<=100:
                    ma.append(x)
                else:
                    print("invalid marks")
            add(na,id,ma)
            print("Student details added successfully")
        case 2:
              def total(ma):
                   print("Total sum=",sum(ma))
              total(ma)
        case 3:
              def percent(ma):
                   x=sum(ma)/5
                   
                   print("total percent",x)
                   return x
              percent(ma)
        case 4:
              def grade(ma):
                   x=sum(ma)/5
                   if 90<=x<=100:
                        print("A+")   
                   elif 80<=x<=89:
                        print("A") 
                   elif 70<=x<=79:
                        print("B")    
                   elif 60<=x<=69:
                        print("B") 
                   elif 50<=x<=59:
                        print("B") 
                   else:
                        print("fail")
              grade(ma)
        case 5:
              print("----------------result------------------")
              add(na,id,ma)
              print()
              total(ma)
              percent(ma)
              grade(ma)
              print("maximum value",max(ma))
              print("minimumm value",min(ma))
        case 6:
              def maxi(ma):
                   print("maximum value",max(ma))
              maxi(ma)
                   
              
        case 7:
              def lis(ma):
                   print("miniimum value",min(ma))
              lis(ma)
                   
              
        case 8:
              print("exit")
              break

