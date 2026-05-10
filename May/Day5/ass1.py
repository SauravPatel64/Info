"""
1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.
"""

cus = input("Enter your  Customer type (Premium / Regular) = ")
amt = int(input("Enter shopping amount = "))


print(f"Final Payable {(amt*80)/100}") if amt>5000 else print(f"Final Payable {(amt*90)/100}")   if cus == "Premium" else print(f"Final Payable {(amt*90)/100}") if amt>3000 else print(f"Final Payable {(amt*95)/100}") 