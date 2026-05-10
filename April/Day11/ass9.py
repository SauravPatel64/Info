"""
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500

"""

D = int(input("Distance = "))
M = int(input("Milage = "))
P = int(input("Petrol Price = "))

liter = D/M

print(f"Cost = {liter * P}")
