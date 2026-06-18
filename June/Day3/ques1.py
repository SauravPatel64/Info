"""
1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

=========================================================
"""

while True:

    print("========menu===============")
    print("1. Add two matrix")
    print("2. subtract two matrix")
    print("3. compare two matrix")
    print("4.exit")
    

    choice=int(input("enter your choice"))
  
    match choice:
        

        case 1:
            rows=int(input("enter no of rows"))
            cols=int(input("enter no of cols"))
            
            print("matrix one")
            mat1=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    x=int(input("enter element"))
                    row.append(x)
                mat1.append(row)
            print("matrix==2")
            mat2=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    x=int(input("enter elelemnt"))
                    row.append(x)
                mat2.append(row)
            
            print("matrix==3" "before addition")
            mat3=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(0)
                mat3.append(row)
            for i in range(len(mat3)):
                for j in range(len(mat3[i])):
                    mat3[i][j]=mat1[i][j]+mat2[i][j]

            print("matrix")
            for i in mat1:
                for j in i:
                    print(j,end=" ")
                print()
            print("matrix=2")
            for i in mat2:
                for j in i:
                    print(j,end=" ")
                print()
            print("matrix==3 after adding of matrix one nd mtrix two")
            for i in mat3:
                for j in i:
                    print(j,end=" ")
                print()
        case 2:
            rows=int(input("enter no of rows"))
            cols=int(input("enter no of cols"))
            print("matrix one")
            mat1=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    x=int(input("enter element"))
                    row.append(x)
                mat1.append(row)
            print("matrix==2")
            mat2=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    x=int(input("enter elelemnt"))
                    row.append(x)
                mat2.append(row)
            
            
            mat3=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(0)
                mat3.append(row)
            for i in range(len(mat3)):
                for j in range(len(mat3[i])):
                    mat3[i][j]=mat2[i][j]-mat1[i][j]

            print("matrix")
            for i in mat1:
                for j in i:
                    print(j,end=" ")
                print()
            print("matrix=2")
            for i in mat2:
                for j in i:
                    print(j,end=" ")
                print()
            print("matrix==3 after Subtractinf  of matrix one nd mtrix two")
            for i in mat3:
                for j in i:
                    print(j,end=" ")
                print()

        case 3:


            if mat1==mat2:
                print("==same matrix ")
            else:
                print("==not same matrix")
        case 4:
            print("exit")
            break
