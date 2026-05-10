
"""
Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h

"""

d = int(input("Enter the Distance : "))
t = int(input("Enter the Time : "))

s = d * t
print(f"Speed = {s} Km/h")