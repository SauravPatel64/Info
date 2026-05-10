"""
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
"""

d=int(input("Distance ="))
m=int(input("Mileage ="))
p=int(input("Petrol price ="))

a=(d/m)
print(f"Petrol Used = {a} litres")

c=(a*p)
print(f"Total Cost = {c} litres")
