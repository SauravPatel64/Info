"""
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
"""


a = int(input("Enter your Marks of Subject A"))
b = int(input("Enter your Marks of Subject B"))
c = int(input("Enter your Marks of Subject C"))

result = float((a+b+c)/3)

print(f"Average : {result}")

