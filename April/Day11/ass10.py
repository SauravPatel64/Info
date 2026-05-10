"""
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
"""

total = int(input("Total = "))
Obtained = int(input("Obtined = "))

P = int((Obtained * 100)/total)

print(f"Percentage = {P}%")