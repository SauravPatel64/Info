"""  
Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0


"""

class Employee:
    
    def __init__(self,employee_id,employee_name,basic_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.basic_salary = basic_salary
        
    def salary(self):
        print(f"Employee ID  : {self.employee_id}")
        print(f"Employee Name  : {self.employee_name}")
        print(f"Basic Salary  : {self.basic_salary}")
        print(f"HRA : {(self.basic_salary*20)/100}")
        print(f"DA  :  {(self.basic_salary*15)/100}")
        print(f"Gross Salary  : {(self.basic_salary) + (self.basic_salary%20/100) + (self.basic_salary*15)/100}")
        
        

s1 = Employee(101, "Saurav_Patel", 5000)
s1.salary()
    