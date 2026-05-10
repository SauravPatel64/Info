"""
10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate

===
"""

m=int(input("Enter marks:"))

if m>=40:
    print("Pass")

if m>=75:
    print("Eligible for certificate")
