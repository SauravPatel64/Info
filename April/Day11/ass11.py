"""
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750

"""

H = int(input("Hours = "))
M = int(input("Minutes = "))
S = int(input("Seconds = "))

totalSeconds = ((H*60*60)+(M*60)+S)
print(f"Total Seconds = {totalSeconds}")