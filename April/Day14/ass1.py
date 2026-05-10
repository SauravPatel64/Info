"""
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75
"""

amt = int(input("Total bill amount = "))
GST = int(input("GST = "))
service = int(input("Service Charge = "))
member = int(input("Number of friends = "))


finalBill = amt + (amt*GST)/100 + (amt*service)/100
Person = finalBill/member

print(f"Final Bill = {finalBill}\nEach Person Pays = {Person}")
 