"""
   
3.MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
"""

while True:
    print("Menu")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")

    rows=int(input("enter no of rows : "))
    cols=int(input("enter no of column: "))
    mat=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            x=int(input("enter element: "))
            row.append(x)
        mat.append(row)
    
    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            print("output: ")
            max=0
            for i in range(len(mat)):
                sum=0
                for j in range(len(mat[i])):
                    n=mat[i][j]
                    sum=sum+n
                if sum>max:
                    max=sum
                    line=i+1
            print("employee",line,"has highest total score",max)
        case 2:
            print("output: ")
            for j in range(cols):
                sum=0
                for i in range(rows):
                    n=mat[i][j]
                    sum=sum+n
                av=sum//cols
                print("month",j+1,"avarage",av)
        case 3:
            print("output: ")
            for i in range(len(mat)):
                max=mat[i][0]
                for j in range(len(mat[i])):
                    n=mat[i][j]
                    if max<n:
                        max=n
                print("employee",i+1,"maximum no",max)
        case 4:
            print("exit")
            break
                   