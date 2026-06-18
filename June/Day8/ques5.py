
"""
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed
    
"""

lib=set()
print()
while True:
    print("Menu:")
    print("1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")

    ch=int(input("enter your choice "))
    match ch:
        case 1:
            n=int(input("enter no if book"))
            for i in range(n):
                x=int(input("enter book ISBN="))
                lib.add(x)

        case 2:
            i=int(input("enter remove ISBN:"))
            if i in lib:
                lib.remove(i)
            else:
                print("not found")
        case 3:
            s=int(input("enter searching ISBN:"))
            if s in lib:
                print("ISBN found")

            else:
                print("NOT FOUND")
        case 4:
            for i in lib:
                print(i,end="  ")
            print()
        case 5:
            print("count=",len(lib))
        case 6:
            print("exit")
            break