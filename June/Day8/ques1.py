"""
1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations
"""



coding=set()
robotic=set()


while True:
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            n=int(input("enter number : "))
            for i in range(n):
                x=int(input("enter id: "))
                coding.add(x)
           
        case 2:
            n=int(input("enter number : "))
            for i in range(n):
                x=int(input("enter id: "))
                robotic.add(x)
        case 3:
            print(coding)
        case 4:
            print(robotic)
        case 5:
            print(coding|robotic)
        case 6:
            print(coding-robotic)
        case 7:
            print(robotic-coding)
        case 8:
            print(coding^robotic)
        case 9:
            print(len(coding^robotic))
        case 10:
            print("exit")
            break
