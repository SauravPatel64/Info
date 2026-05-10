


"""
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0


"""

principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate (%): "))
time = float(input("Enter Time (years): "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Amount =", amount)
print("Compound Interest =", compound_interest)