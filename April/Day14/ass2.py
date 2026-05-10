"""
Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

"""

price, downPayment = map(int,input("Enter your Mobile Price and Down payment = ").split())
rate = int(input("Interest rate = "))
Months = int(input("Months = "))

print(f"Remaining Amount = {price - downPayment}\nTotal with Interest = {int((price - downPayment)*110/100)}\nMonthly EMI = {((price - downPayment)*110/100)/10}")