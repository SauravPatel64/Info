"""
Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
"""

cp = int(input("Cost Price = "))
sp = int(input("Selling Price = "))

p = int(sp-cp)

profit = ((p*100)/cp)

print(f"Profit = {p}\n Profit % = {profit}")