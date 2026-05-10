amt = int(input("Enter total Card price: "))

Tax = int((amt*12)/100)

Total = int(amt + Tax)

print(f"Cart = {amt}, \n Tax = {Tax}, \n Total = {Total}")