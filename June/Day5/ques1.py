"""
=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
"""



from collections import namedtuple
employee=namedtuple("employee",["emp_id","emp_name","department","salary"])
n=int(input("enter n: "))
emp=[]
for i in range(n):
    id=int(input("enter your id"))
    name=input("enter name")
    d=input("enter department ")
    s=int(input("enter salary"))
    emp.append(employee(id,name,d,s))

for i in emp:
    for j in i:
        print(j,end=" ")
    print()


#highets

print()
print("highest salary employee")
hs=0
hse=0
for i in range(len(emp)):
    if emp[i][3]>hs:
        hs=emp[i][3]
        hse=i
for j in range(len(emp[hse])):
    print(emp[hse][j],end=" ")

#lowest 
print()
print("lowesr salary employee")
ls=emp[0][3]
ise=0
for i in range(len(emp)): 
    if emp[i][3]<ls:
        ls=emp[i][j]
        ise=i
for j in range(len(emp[ise])):
    print(emp[ise][j],end=" ")
print()
print()
#avarage
sum=0
print()
for i in range(len(emp)):
    a=emp[i][3]
    sum=sum+a
print("avarage salary")
print("avarage",sum//len(emp))    

#department
d=input("enter your department: ")
print("employee in ",d,"department")
c=0
for i in range(len(emp)):
    a=emp[i][2]
    if a==d:
        for j in range(len(emp[i])):
            print(emp[i][j],end=" ")
        print()
