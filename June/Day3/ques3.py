
        
"""
3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

=========================================================
"""

while True:
    print("1. Count Armstrong Numbers Row-wise")
    print("2. Count Palindrome Numbers Column-wise")
    print("3. Display Average of Each Row")
    print("4. Exit")

    rows=int(input("enter no of rows"))
    cols=int(input("enter no of "))

    mat=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            x=int(input("enter element "))
            row.append(x)
        mat.append(row)
    choice=int(input("enter youe choice : "))

    match choice:
        case 1:
            print("output :")
            for i in range(cols):
                c=0
                for j in range(rows):

                    n=mat[j][i]
                    rev=0
                    temp=n
                    while n>0:
                        rem=n%10
                        rev=rev*10+rem
                        n=n//10
                    else:
                      if rev==temp:
                        c=c+1
                print("column",i+1,"plaindrome count",c)
        case 2:
            print("output : ")
            for i in range(len(mat)):
                c=0
                for j in range(len(mat[i])):
                    n=mat[i][j]
                    b=n
                    sum=0
                    while n>0:
                        rem=n%10
                        sum=sum+rem**len(str(b))
                        n=n//10
                    else:
                        if sum==b:
                            c=c+1
                print("row",i+1,"armstrong count",c)
        case 3:
            for i in range(len(mat)):
                sum=0
                for j in range(len(mat[i])):
                    n=mat[i][j]
                    sum=sum+n

                else:
                    av=sum//len(mat[i])
                print("row",i+1,"avareage",av)