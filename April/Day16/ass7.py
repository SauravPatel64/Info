"""
7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable

===
"""

s=int(input("Enter salary:"))

if s>=30000:
    print("PF applicable")
if s>=50000:
    print("Bonus applicable")
