"""
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
"""
pnr = input("Enter PNR: ")

if not pnr.startswith("PNR"):
    print("Invalid PNR Number")

elif len(pnr) != 12:
    print("Invalid PNR Number")

elif not pnr[3:].isdigit():
    print("Invalid PNR Number")

else:
    print("Valid PNR Number")