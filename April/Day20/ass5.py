"""
5. Cinema Ticket Booking System


A cinema hall charges ticket prices based on the age of the customer:

* Children (below 12 years) → ₹100
* Adults (12 to 60 years) → ₹200
* Senior citizens (above 60 years) → ₹150

Write a Python program to determine the ticket price.

Input:
Enter age: 10

Output:
Ticket Price: ₹100

"""

age = int(input("Enter age:"))

if age < 12:
    print(f"Ticket Price: ₹{100}")
elif age > 12 and age < 60:
    print(f"Ticket Price: ₹{200}")
else:
    print(f"Ticket Price: ₹{150}")