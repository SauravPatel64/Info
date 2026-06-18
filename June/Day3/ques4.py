
"""
4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

=========================================================
                       
"""

while True:
    print("1. Display Main Diagonal Elements")
    print("2. Display Secondary Diagonal Elements")
    print("3. Compare Main and Secondary Diagonal Sums")
    print("4. Exit")

    rows=int(input('enter no of rows: '))
    cols=int(input("enter no of column: "))
    mat=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            x=int(input("enter element : "))
            row.append(x)
        mat.append(row)
    
    choice=int(input("enter your choice : "))

    match choice:
        case 1:
            if rows==cols:

                for i in range(len(mat)):
                    print(mat[i][i],end=" ")
                print()
            else:
                print("daigonal are not found")
        case 2:
            if rows==cols:

                for i in range(cols):
                    print(mat[i][cols-i-1],end=" ")
                print()

            else:
                print("daigonal are not found ")
        case 3:
            sum=0
            sum1=0
            for i in range(cols):
                sum=sum+mat[i][i]
            for i in range(cols):
                sum1=sum1+mat[i][cols-i-1]
            print("Main Diagonal Sum",sum)
            print("Secondary Diagonal Sum",sum1)

            if sum==sum1:
                print("Both Diagonal Sums are Equal")
            else:
                print("not same")
        case 4:
            print("exit")
            break
