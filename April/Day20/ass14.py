"""
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000

"""

Programming = 5000
Design = 4000
Marketing = 3000

course = input("Enter course category: ")
user = input("Enter user type: ")

if course == "Programming":
    if user=="Student":
        print(f"Final Course Fee: ₹{int(Programming*80/100)}")
    elif user=="Working":
        print(f"Final Course Fee: ₹{int(Programming*90/100)}")
    else:
        print(f"Final Course Fee: ₹{Programming}")

elif course == "Design":
    if user=="Student":
        print(f"Final Course Fee: ₹{int(Design*80/100)}")
    elif user=="Working":
        print(f"Final Course Fee: ₹{int(Design*90/100)}")
    else:
        print(f"Final Course Fee: ₹{Design}")

elif course == "Marketing":
    if user=="Student":
        print(f"Final Course Fee: ₹{int(Marketing*80/100)}")
    elif user=="Working":
        print(f"Final Course Fee: ₹{int(Marketing*90/100)}")
    else:
        print(f"Final Course Fee: ₹{Marketing}")





