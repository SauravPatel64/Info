"""
Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3

"""
amt = int(input("Amount = "))

Hund = int(amt/100)

Fifty = int((amt - (Hund*100))/50)

Tens = int((amt - ((Hund*100) + (Fifty *50)))/10)

print(f"₹100 x {Hund}\n₹50 x {Fifty}\n₹10 x {Tens}")