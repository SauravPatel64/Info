


restaurant_name = input("Enter Restaurant Name: ")

pizza_price = int(input("Enter Pizza Price: "))
burger_price = int(input("Enter Burger Price: "))
pasta_price = int(input("Enter Pasta Price: "))
coffee_price = int(input("Enter Coffee Price: "))

total_bill = 0

while True:

    print("\n===== Welcome to", restaurant_name, "=====")
    print("1. Pizza")
    print("2. Burger")
    print("3. Pasta")
    print("4. Coffee")
    print("5. Generate Bill")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            qty = int(input("Enter Pizza Quantity: "))
            total_bill = total_bill + (qty * pizza_price)
            print("Pizza Added Successfully")

        case 2:
            qty = int(input("Enter Burger Quantity: "))
            total_bill = total_bill + (qty * burger_price)
            print("Burger Added Successfully")

        case 3:
            qty = int(input("Enter Pasta Quantity: "))
            total_bill = total_bill + (qty * pasta_price)
            print("Pasta Added Successfully")

        case 4:
            qty = int(input("Enter Coffee Quantity: "))
            total_bill = total_bill + (qty * coffee_price)
            print("Coffee Added Successfully")

        case 5:

            print("\n===== Final Bill =====")
            print("Total Bill:", total_bill)

            if total_bill >= 1000:

                discount = total_bill * 0.10
                final_amount = total_bill - discount

                print("Discount Applied: 10%")
                print("Discount Amount:", discount)
                print("Final Amount:", final_amount)

            else:
                print("No Discount Applied")
                print("Final Amount:", total_bill)

            print("\nThank You Visit Again")
            break

        case _:
            print("Invalid Choice")