""" 2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []

"""
n=int(input("Enter no. of employee:"))
a=[]
for i in range(n):
    x=int(input("Enter salary:"))
    a.append(x)
print(a)
l=len(a)
sum=0
above=0
for i in a:
    sum=sum+i
    s=(sum/l)
    if i > s:
        greater=s
    if i <= 15000:
        z=i
    else:
        above=i
print("Average:",s)
print("Above average:",greater)
print("remaining List:",above)