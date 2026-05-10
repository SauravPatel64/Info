"""
9. Smart Loan Eligibility System

A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%
"""


salary = int(input("Salary = "))
age = int(input("Age = "))
credit_score = int(input("Credit Score = "))
emi = int(input("EMI = "))


if salary >= 40000:
    if 21 <= age <= 60:
        if credit_score >= 750:
            if emi <= (0.4 * salary):
                status = "Approved at 8%"
            else:
                status = "Approved at 10%"
        elif credit_score >= 650:
            status = "Approved at 12%"
        else:
            status = "Rejected"
    else:
        status = "Rejected" # Age out of eligible range

else:
    if salary >= 25000 and credit_score >= 700:
        status = "Approved at 13%"
    else:
        status = "Rejected"


print(f"Loan Status = {status}")