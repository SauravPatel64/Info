"""
4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.
"""

unit = int(input("Enter your  units = "))

bill = unit*5 if unit <= 100 else ((100*5)+ (unit-100)*7) if (unit>=101 or unit <=300) else ((200*7)+(100*5)+ (unit-300)*10)

print(f"Total Bill = {bill}")