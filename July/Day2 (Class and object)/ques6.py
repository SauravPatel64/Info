""" 
Library Book Management System


A library wants to maintain information about books. The librarian should be able to:

View book details.
Issue the book to a student.
Return the book.
Requirements

Create a class named Book with the following attributes:

book_id
title
author
status (Initially "Available")

Initialize the values using a constructor.

Create the following methods:
display_details() → Displays all book information.
issue_book() → Changes the status to "Issued".
return_book() → Changes the status to "Available".
Sample Input
Enter Book ID : B101
Enter Book Title : Python Programming
Enter Author Name : John Smith
Sample Output
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available

Book issued successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Issued

Book returned successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available
"""

















class Book:
    def __init__(self, book_id, title, author):
        """Initializes the book details with a default status of 'Available'."""
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "Available"

    def display_details(self):
        """Displays all book information."""
        print("------ Book Details ------")
        print(f"Book ID     : {self.book_id}")
        print(f"Title       : {self.title}")
        print(f"Author      : {self.author}")
        print(f"Status      : {self.status}\n")

    def issue_book(self):
        """Changes the status to 'Issued' if it's currently available."""
        if self.status == "Available":
            self.status = "Issued"
            print("Book issued successfully.\n")
        else:
            print(f"Sorry, this book is already issued (Current Status: {self.status}).\n")

    def return_book(self):
        """Changes the status back to 'Available'."""
        if self.status == "Issued":
            self.status = "Available"
            print("Book returned successfully.\n")
        else:
            print("This book is already available in the library.\n")


if __name__ == "__main__":
    book_id = input("Enter Book ID : ")
    title = input("Enter Book Title : ")
    author = input("Enter Author Name : ")
    print()  # For spacing

    my_book = Book(book_id, title, author)

    my_book.display_details()

    my_book.issue_book()
    my_book.display_details()

    my_book.return_book()
    my_book.display_details()