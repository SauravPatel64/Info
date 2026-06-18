
"""
3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations
Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations

"""
n=int(input("enter no  of id's:"))
x=0
s=set()
while True:
    print("Menu:")
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")


    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            
            for i in range(n):
                x=int(input("enter element"))
                s.add(x)
        case 2:
            idd=int(input("enter item to remove"))
            if idd in s:
                s.remove(idd)
                print("visitor removed successfully")
            else:
                print("not found")
        case 3:
            id=int(input("enter your id"))
            if id in s:
                print("visitor exixts")
            else:
                print("not found")
        case 4:
            print("visitor :",s)
        case 5:
            print(len(s))
        case 6:
            s.clear()
            print(s)
        case 7:
            print("exist")
            break