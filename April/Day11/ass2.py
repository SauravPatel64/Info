"""
Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000

"""

Daily_wages = int(input("Please  Enter your daily wages : "))
Days = int(input("Please Enter the total no of Day Have you work : "))
salary = Daily_wages * Days
print(f"Salary = {salary}")