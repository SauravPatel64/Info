"""
5.

====================================================================
 Student Classroom Matrix Analysis
====================================================================

Scenario

A school stores student marks in a matrix.

Rows represent different classrooms.
Columns represent students in each classroom.

The principal wants to analyze the performance of each classroom by
calculating the total marks scored by students in every row.

Requirements

* Read number of rows from user
* Read number of columns from user
* Read all matrix elements from user
* Display the complete matrix
* Find Row Wise Sum
* Display sum of each row separately

Test Case 1

Input:

Rows = 3
Columns = 3

Matrix:

10 20 30
40 50 60
70 80 90

Output:

Matrix:

10 20 30
40 50 60
70 80 90

Row 1 Sum = 60
Row 2 Sum = 150
Row 3 Sum = 240

------------------------------------------------------------

Test Case 2

Input:

Rows = 2
Columns = 4

Matrix:

1 2 3 4
5 6 7 8

Output:

Matrix:

1 2 3 4
5 6 7 8

Row 1 Sum = 10
Row 2 Sum = 26

------------------------------------------------------------

Test Case 3

Input:

Rows = 2
Columns = 2

Matrix:

100 200
300 400

Output:

Matrix:

100 200
300 400

Row 1 Sum = 300
Row 2 Sum = 700

------------------------------------------------------------

Additional Challenge

Also Display:

* Row Wise Sum
* Row Wise Average
* Row Having Maximum Sum
* Grand Total of Matrix

Sample Output

===== MATRIX REPORT =====

Matrix:

10 20 30
40 50 60
70 80 90

Row 1 Sum = 60
Row 2 Sum = 150
Row 3 Sum = 240

Row 1 Average = 20.0
Row 2 Average = 50.0
Row 3 Average = 80.0

Maximum Sum Row = Row 3
Grand Total = 450
"""

rows=int(input("enter no pf rows"))
cols=int(input("enter no of column"))
mat=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input("enter element"))
        row.append(x)
    mat.append(row)
print(mat)
print("matrix")
max=0
r=0
gt=0
for i in range(len(mat)):
    sum=0
    for j in range(len(mat[i])):
        e=mat[i][j]
        sum=sum+e

    print("row",i+1,"sum=",sum)
    print("row",i+1,"average",sum/len(mat[i]))
    gt=gt+sum
    print()
    if max<sum:
        max=sum
        r=i+1
print("maximum sum row",r)
print("grand total",gt)

     