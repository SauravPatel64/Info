"""
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
"""


amt = int(input("Enter the Amount : "))
Discount = (amt*10)/100

Final = amt - Discount

print(f"Discount = {Discount} \n Final = {Final}")