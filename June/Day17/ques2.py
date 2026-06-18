
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