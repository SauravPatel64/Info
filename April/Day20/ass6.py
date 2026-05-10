"""

6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000

"""

salary = int(input("Enter salary: "))
experience = int(input("Enter years of experience: "))

if experience > 10:
    print(f"Bonus Amount : ₹{int(salary*20/100)}")
elif experience >5 and experience <10:
    print(f"Bonus Amount : ₹{int(salary*10/100)}")
elif experience >2 and experience <5:
    print(f"Bonus Amount : ₹{int(salary*10/100)}")
else:
    print(f"Bonus Amount : No bonus")