
"""
=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 70
"""


from collections import namedtuple
n=int(input("enter no of book: "))
library=namedtuple("library",["book_id","title","author","price"])
book=[]
for i in range(n):
    bid=int(input("enter book id")) 
    bt=input("enter title")
    a=input("enput author ")
    p=int(input("enter price "))
    book.append(library(bid,bt,a,p))
for i in book:
    for j in i:
        print(j,end=" ")
    print()

#most expensive book
print("most expensive book:")
max=0
h=0
for i in range(len(book)):
    a=book[i][3]
    if max<a:
        max=a
        h=i

for j in range(len(book[h])):
    print(book[h][j],end=" ")

#avarage
print()
av=0
sum=0
for i in range(len(book)):
    a=book[i][3]
    sum=sum+a
print("avarage book price")
print(sum//len(book))

#find book through auther
d=input("enter auther")
for i in range(len(book)):
    
    if book[i][2]==d:
        for j in range(len(book[i])):
            print(book[i][j],end=" ")
        print()