"""
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System

"""
"""
n=int(input("enter no patients: "))
d={}

for i in range(n):
    d2={}
    id=int(input("enter pateint id"))
    d[id]=d2
    for i in range(4):
        k1=input("enter your key ")
        va=input("enter value: ")
        
        if k1=="age":
            va=int(va)
        d2[k1]=va

print(d)
while True:
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")

    ch=int(input("enter your choice "))
    match ch:
        case 1:
            
            np={}
            id=int(input("enter new patient id: "))
            if id not in d:
                d[id]=np
                name=input("enter patient name ")
                np["name"]=name
                age=int(input("enter patient name"))
                np["age"]=age
                disease=input("enter disease name: ")
                np["disease"]=disease
                dr=input("enter dr name: ")
                np["dr name"]=dr
            else:
                print("id already exist")
        case 2:
            sr=int(input("enter searching patient: "))
            if sr in d:
                print("patient id:",sr)
                for k,v in d[sr].items():
                    print(k,":",v)
        case 3:
            id=int(input("enter patient id: "))
            nd=input("update your new disease")
            if id in d:
                d[id]["disease"]=nd
            print("Disease Updated Successfully")



        case 4:

            de=int(input("enter detet item id: "))
            if de in d:
                del d[de]
                print("Patient Record Deleted Successfully")
            else:
                print("id not found")
        case 5:
            print("Display All Patients")
            print("====================")
            for k,v in d.items():
                print("id=",k)
                for k1,v1 in v.items():
                    print(k1,":",v1)
                print("=========================")
        case 6:
            print("patient count",len(d))
        case 7:
            de=input("enter disease: ")
            f=0
            for i in  d:
                
                    if de==d[i]["disease"]:
                        print(i,d[i]["name"])
                        f=1
                
            else:
                if f==0:
                    print("no patient found")
        case 8:
            oa=0
            for i in d:
                if d[i]["age"]>oa:
                    oa=d[i]["age"]
                    o=i
            print("oldesr patient detail: ")
            print()
            print("patient id",o)
            for k,v in d[o].items():
                print(k,":",v)
        case 9:
            la=0
            for i in d:
                if d[i]["age"]>la:
                    la=d[i]["age"]
                    o=i
            print("lowest patient detail: ")
            print()
            print("patient id",o)
            for k,v in d[o].items():
                print(k,":",v)

        case 10:
            print("Thank You For Using Hospital Patient Management System")
            break

"""



"""
2.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System

"""
"""
d={
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}

while True:           
    print("1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10. Find Student Paying Lowest Fees")
    print("11. Exit ")
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            n=int(input("enter no of student: "))
            d1={}
            for i in range(n):
                id=int(input("enter your id"))
                if id not in d:
                    d[id]=d1
                    name=input("enter student name")
                    d1["name"]=name
                    course=input("enter course name")
                    d1["course"]=course
                    mn=int(input("enter mobile no"))
                    d1["mobile"]=mn
                    fees=int(input("enter fees"))
                    d1["fees"]=fees
                    city=input("enter city")
                    d1["city"]=city
                else:
                    print("patient id already exist")
        case 2:
            sr=int(input("enter student id: "))
            if sr in d:
                print("id",sr)
                for k,v in d[sr].items():
                    print(k,":",v)
            else:
                print("id not found")
        case 3:
            id=int(input("entre your id"))
            if id in d:
                c=input("enter yoyr course")
                d[id]["course"]=c
                print("course update successfully")
            else:
                print("id not found")
        case 4:
            id=int(input("enter your id for delete"))
            if id in d:
                del d[id]
                print("Student Deleted Successfully")
            else:
                print("student not found")
        case 5:
            print("STUDENT")
            for k,v in d.items():
                print("id=",k)
                for k1,v1 in v.items():
                    print(k1,":",v1)
        case 6:
            print("total no of student =",len(d))
        case 7:
            c=input("enter your course: ")
            f=0
            for i in d:
                if c==d[i]["course"]:
                    print(i,d[i]["name"])
        case 8:
            ci=input("enter city : ")
            for i in d:
                if d[i]["city"]==ci:
                    print(i,d[i]["city"])
        case 9:
            print("highest fees")
            max=0
            for i in d:
                a=d[i]["fees"]
                if a>max:
                    max=d[i]["fees"]
                    h=i
            print("id",h)
            for k,v in d[h].items():
                print(k,":",v)
                
        case 10:
            print("lowest salary: ")
            low=d[101]["fees"]
            
            for j in d:
                a=d[j]["fees"]
                if low>a:
                    low=a
                    h=j
            print("id",h)
            for k,v in d[h].items():
                print(k,":",v)


        
        
        
"""