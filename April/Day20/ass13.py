"""
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600

"""

salary = int(input("Enter salary: "))
rating = int(input("Enter rating: "))



if rating== 5:
    if salary < 20000:
        print(f"Revised Salary: {int(salary + (salary*25/100) + 2000)}")
    else:
        print(f"Revised Salary: {int(salary + (salary*25/100))}")
elif rating == 4:
    print(f"Revised Salary: {int(salary + (salary*20/100)+2000)}")
elif rating == 3:
    print(f"Revised Salary: {int(salary + (salary*10/100))}")
elif rating == 2:
    print(f"Revised Salary: {int(salary + (salary*5/100))}")
else:
    if rating==1:
        print(f"Revised Salary: {int(salary)} No Hike")