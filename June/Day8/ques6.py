
"""
6.

=========================================
COMMON CHARACTER FINDER
=========================================

Enter two strings and find common characters.

Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}

"""


while True:
    print("Menu:")
    print("1. Enter First String")
    print("2. Enter Second String")
    print("3. Display Common Characters")
    print("4. Count Common Characters")
    print("5. Exit")

    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            n1=input("enter firdt string")
            s=set(n1)
        case 2:
            n2=input("enter seconf string")
            s1=set(n2)

        case 3:
            print("common character",s.intersection(s1))
        case 4:
            print("common character count",len(s&s1))
        case 5:
            print("exit")
            break
