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