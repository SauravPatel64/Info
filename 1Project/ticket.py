

train_name = input("Enter Train Name: ")
available_seats = int(input("Enter Total Available Seats: "))
ticket_price = int(input("Enter Ticket Price: "))

while True:

    print("\n===== Railway Ticket Booking System =====")
    print("1. Check Train Details")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Check Available Seats")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("\nTrain Name:", train_name)
            print("Ticket Price:", ticket_price)

        case 2:
            seats = int(input("Enter number of seats to book: "))

            if seats <= available_seats:

                total_amount = seats * ticket_price
                available_seats = available_seats - seats

                print("\nTicket Booked Successfully")
                print("Booked Seats:", seats)
                print("Total Amount:", total_amount)
                print("Remaining Seats:", available_seats)

            else:
                print("\nSeats Not Available")

        case 3:
            cancel = int(input("Enter number of tickets to cancel: "))

            available_seats = available_seats + cancel

            print("\nTicket Cancelled Successfully")
            print("Updated Seats:", available_seats)

        case 4:
            print("\nAvailable Seats:", available_seats)

        case 5:
            print("\nThank You")
            break

        case _:
            print("\nInvalid Choice")