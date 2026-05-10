"""
9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible
"""

percentage =  int(input("Enter attendance percentage: "))

if percentage >= 75:
    print("Status: Eligible")
elif percentage >= 60 and percentage <= 74:
    print("Status: Eligible with warning")
else:
    print("Status: Not eligible")
