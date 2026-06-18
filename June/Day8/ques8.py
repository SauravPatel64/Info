
"""
8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters

"""

allowed = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
)

username = ""

while True:
    print("\nMenu:")
    print("1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            username = input("Enter Username: ")

        case 2:
            if set(username).issubset(allowed):
                print("Valid Username")
            else:
                print("Invalid Username")

        case 3:
            print("Allowed Characters:")
            for i in allowed:
                print(i, end=" ")
            print()

        case 4:
            print("Exit")
            break

        case _:
            print("Invalid Choice")

