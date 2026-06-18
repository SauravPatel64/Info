
"""
4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed

"""


s=frozenset(["Python","Java","MySQL","React","Spring Boot"])
while True:
    print("Menu:")
    print("1. Display Subjects")
    print("2. Search Subject")
    print("3. Count Subjects")
    print("4. Attempt to Add Subject")
    print("5. Exit")
    ch=int(input("enter your choice:"))
    match ch:
        case 1:
            for i in s:
                print( i,end= " , ")
        case 2:
            sr=input("enter your subject: ")
            if sr in s:
                print("suject exist ")
            else:
                print("subject not found")
        case 3:
            print("count=",len(s))
        case 4:
            print("cannot add subjevt because frozen set is immutable ")
        case 5:
            print("exit")
            break

