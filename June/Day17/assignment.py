print("hello guys how are you")
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
              """
"""
2.
NUMBER ANALYSIS SYSTEM

Scenario:

A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit

Requirements

Choice 1 – Check Perfect Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return True if the number is Perfect, otherwise False.
* Display an appropriate message based on the returned value.

Choice 2 – Check Prime Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return a message such as "Prime Number" or "Not a Prime Number".
* Display the returned message.

Choice 3 – Find Reverse of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return the reversed number.
* Display the returned value.

Choice 4 – Calculate Factorial

* Accept a number from the user.
* Pass the number to a function.
* The function should return the factorial value.
* Display the returned value.

Choice 5 – Display Factors of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return all factors of the given number.
* Display the returned factors.

Choice 6 – Exit

Sample Output

Enter Choice : 1

Enter Number : 28

28 is a Perfect Number

---

Enter Choice : 2

Enter Number : 17

Prime Number

---

Enter Choice : 3

Enter Number : 1234

Reverse Number : 4321

---

Enter Choice : 4

Enter Number : 5

Factorial : 120

---

Enter Choice : 5

Enter Number : 12

Factors : 1 2 3 4 6 12

---

Important Instructions

1. Create separate functions for each operation.
2. Use parameters to pass values to functions.
3. Use return statements appropriately.
4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
5. Avoid using global variables.
6. Implement the solution using a menu-driven approach.
7. Write meaningful function names and maintain proper code readability.
"""
"""
while True:
    print("1. Check Perfect Number")
    print("2. Check Prime Number")
    print("3. Find Reverse of a Number")
    print("4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. Exit")
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            def pn(n):
                sum=0
                for i in range(1,n):
                    if n%i==0:
                        sum=sum+i
                    else:
                        pass
                else:
                    if n==sum:
                        print(n,"perfect no")
                    else:
                        print(n,"not a perfect no")
            n=int(input("enter number"))
            pn(n)
        case 2:
            def prino(m):
                x=0
                
                for i in range(2,m//2+1):
                        if m%i==0:
                            x=1
                            break
                
                if x==0:
                            print("prime no")
                else:
                            print("not a prime no")

            m=int(input("enter prime no"))
            prino(m)
        case 3:
            n=int(input("enter your no"))
            def rev(n):
                r=0
                while n>0:
                    rem=n%10
                    r=r*10+rem
                    n=n//10
                print("reverse no",r)
            rev(n)
        case 4:
            n=int(input("enter factorial no "))
            def fac(n):
                f=1
                for i in range(1,n+1):
                    f=f*i
                print("factorial =",f)
            fac(n)
        case 5:
            def fact(n):
                for i in range(1,n+1):
                    if n%i==0:
                        print(i,end=" ")
            n=int(input("enter no"))
            fact(n)
            print()
        case 6:
            print("exit")
            break
"""

"""
3.
ONLINE SHOPPING SYSTEM

Scenario:

An e-commerce company wants to develop an Online Shopping System. The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU

1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit

Requirements

Choice 1 – Customer Registration

* Accept Customer Name, Email, and Mobile Number.
* Pass the values to a function using Positional Arguments.
* Display the registered customer details.

Choice 2 – Product Information

* Accept Product Name, Price, and Category.
* Call the function using Keyword Arguments.
* Display the product details.

Choice 3 – Generate Invoice

* Accept Product Name and Price.
* Tax Percentage should have a default value.
* Use Default Arguments while generating the invoice.
* Display the final amount.

Choice 4 – Add Multiple Products

* Allow the user to enter any number of product prices.
* Pass all prices to a function using Variable Length Arguments (*args).
* Calculate and display the total bill amount.

Choice 5 – Display Customer Profile

* Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
* Pass the details using Arbitrary Keyword Arguments (**kwargs).
* Display all customer information.

Choice 6 – Exit

Sample Execution

Enter Choice : 1

Enter Name : Ajay
Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
Enter Mobile : 9876543210

Customer Registered Successfully

---

Enter Choice : 2

Enter Product Name : Laptop
Enter Price : 55000
Enter Category : Electronics

Product Details Displayed Successfully

---

Enter Choice : 3

Enter Product Name : Laptop
Enter Price : 55000

Invoice Generated Successfully

---

Enter Choice : 4

Enter Number of Products : 4

Enter Price 1 : 100
Enter Price 2 : 200
Enter Price 3 : 300
Enter Price 4 : 400

Total Bill Amount : 1000

---

Enter Choice : 5

Customer Profile Displayed Successfully

---

Enter Choice : 6

Thank You. Program Terminated.

Important Instructions

1. Choice 1 must use Positional Arguments.
2. Choice 2 must use Keyword Arguments.
3. Choice 3 must use Default Arguments.
4. Choice 4 must use Variable Length Arguments (*args).
5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
6. Use separate functions for each menu option.
7. Implement the solution using a menu-driven approach.
8. Maintain proper code readability and formatting.

Note:
Marks will be awarded based on the correct usage of the specified argument type in each menu option


  """              
while True:
    print("1. Customer Registration")
    print("2. Product Information")
    print("3. Generate Invoice")
    print("4. Add Multiple Products")
    print("5. Display Customer Profile")
    print("6. Exit")
    ch=int(input("enter your choice: "))

    match ch:
        case 1:
            def cr(name,email,mb,/):
                print("Name :",name)
                print("email :",email)
                print("mobile_no :",mb)
            n=input("enter your name")
            em=input("enter your email")
            mb=int(input("enter mobile no"))
            cr(n,em,mb)
            print("Customer Registered Successfully")
        case 2:
            def pi(pn,p,c):
                print("product name:",pname)
                print("price:",pri)
                print("category",cat)
            pname=input("enter product name")
            pri=int(input("enter price"))
            cat=input("enter category")
            pi(p=pri,pn=pname,c=cat)
            print("Product Details Displayed Successfully")

        case 4:
            def pro(l):
                for i in range(len(l)):
                    print("price",i+1,l[i])
                print("total",sum(l))
            n=int(input("enter no of product:"))
            l=[]
            for i in range(n):
                x=int(input("enter element:"))
                l.append(x)
            pro(l)
        case 5:
            def profile(**kwargs):
                for k,v in kwargs.items():
                    print(k,":",v)
            n=input("enter name")
            c=input("entre city")
            e=input("enter email")
            m=int(input("enter mobile"))
            mt=input("enter membership type")
            profile(name=n,city=c,email=e,mobile=m,membership_type=mt)
        case 6:
            print("exit")
            break