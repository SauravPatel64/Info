"""
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
"""

monthly,days, hours = map(int,input(" Monthly Salary , Working days, working hour per days ").split())

per_Day = monthly/days

print(f"Salary per day = {per_Day}\nSalary per hour = {per_Day/hours}")