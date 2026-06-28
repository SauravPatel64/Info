#question==1
"""
Employee Data Processing System

A company stores information about its employees in two forms:

A list of employee ages.
A string containing employee names separated by spaces.

The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.

Problem Statement

Develop a menu-driven Python application called Employee Data Processing System.

The program should allow the HR department to perform the following operations:

Functions on Employee Ages (List)
1. find_second_highest_age(age_list)
Accept a list of employee ages.
Return the second highest age.
2. count_senior_employees(age_list)
Accept a list of employee ages.
Consider employees aged 50 years or above as senior employees.
Return the count of senior employees.
3. remove_duplicate_ages(age_list)
Accept a list of employee ages.
Return a new list after removing duplicate ages while maintaining the original order.
Functions on Employee Names (String)
4. count_names_starting_with_vowel(names)
Accept a string containing employee names separated by spaces.
Return the number of names that start with a vowel (A, E, I, O, U).
5. longest_name(names)
Accept a string containing employee names separated by spaces.
Return the employee name having the maximum number of characters.
Menu
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
Enter your choice:
Sample Input
Employee Ages:
34 55 29 60 55 42 60 51

Employee Names:
Ajay Rahul Esha Omkar Ishita Neha
Sample Output
Second Highest Age : 55
Senior Employees : 4
Unique Ages : [34, 55, 29, 60, 42, 51]
Names Starting with Vowel : 3
Longest Employee Name : Ishita
Instructions
Implement all operations using separate functions.
Each function must accept parameters and return the result.
Do not print results inside the functions.
The menu should continue to appear until the user selects Exit.
Display an appropriate message for an invalid choice.
Use meaningful function and variable names and follow proper indentation
"""

def age(l):
    l=sorted(l)
    return l[-2]

def cl(l):
    c=0
    for i in l:
        if i>=50:
            c=c+1
    return c


def remove(l):
    r=set(l)
    return r

def vowel(n):
    c=0
    for i in n:
        if i.lower().startswith(("a", "e", "i", "o", "u")):
            c=c+1
    return c
from functools import reduce
def long(n):
    f=reduce(lambda x,y:x if len(x)>len(y) else y,n)
    return f


while True:
    print("========== EMPLOYEE DATA PROCESSING SYSTEM ==========")
    print("1. Find Second Highest Employee Age")
    print("2. Count Senior Employees")
    print("3. Remove Duplicate Ages")
    print("4. Count Names Starting with a Vowel")
    print("5. Find Longest Employee Name")
    print("6. Exit")
    ch=int(input("enter choice: "))
    match ch:
        case 1:
             l=list(map(int,input("enter your age: ").split()))
             print("second highest employee age",age(l))
        case 2:
             l=list(map(int,input("enter your age: ").split()))
             print("senior count",cl(l))
        case 3:
            l=list(map(int,input("enter your age: ").split()))
            print("remove duplicate value:",remove(l))
        case 4:
            n=list(map(str,input("enter your name: ").split()))
            print("name startswith vowel",vowel(n))
        case 5:
            n=list(map(str,input("enter your name: ").split()))
            print("longest name",long(n))



        case 6:
            print("exit")
            break

