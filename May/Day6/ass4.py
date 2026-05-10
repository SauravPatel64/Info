"""

4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

---


"""


print("1 → Enter Units Consumed\n2 → Calculate Bill Amount\n3 → Apply Surcharge\n4 → Display Final Bill")
a = int(input("Enter your Choice : "))
unit = 0
amt = 0

if a == 1:
    unit = int(input("Enter units consumed: "))
    print("Units recorded successfully")
    
    print("1 → Enter Units Consumed\n2 → Calculate Bill Amount\n3 → Apply Surcharge\n4 → Display Final Bill\n5 → Exit")

    while True:
        print()
        print()
        b = int(input("Enter your choice : "))
        match b:
            case 1:
                print("Units recorded successfully")

            case 2:
                amt = (unit * 5) if unit <= 100 else (100 * 5 + (unit - 100) * 7) if unit <= 200 else (
                            100 * 5 + 100 * 7 + (unit - 200) * 10)
                print(f"Bill Amount: {amt}")

            case 3:
                supCharge = amt * 10 % 100 if amt > 2000 else amt * 5 % 100
                print(f"Super Charge = {supCharge}")

            case 4:
                supCharge = amt * 10 % 100 if amt > 2000 else amt * 5 % 100
                print("----- Final Bill -----")
                print(f"Units: {unit}\nBill Amount: {amt}\nSurCharge: {supCharge}\nTotal Payable: {amt + supCharge}")

            case 5:
                while b == 5:
                    print("Exiting system... Thank you!")
                    break
            case _:
                print("Invalid choice. Please try again.")


else:
    print("Please enter units consumed first")
    a=2
        



