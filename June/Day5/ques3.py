


"""
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
"""

from collections import namedtuple
n=int(input("enter patient count= "))
pat=namedtuple("patients",["patient_id","patients_name","age","disease"])
p=[]
for i in range(n):
    pid=int(input("enter patient id: "))
    name=input("enter patient name: ")
    age=int(input("enter patient age: "))
    dise=input("enter patient disease: ")
    p.append(pat(pid,name,age,dise))
for i in p:
    for j in i:
        print(j,end=" ")
    print()

#find patient 
f=int(input("enter finding id: "))
for i in range(len(p)):
    a=p[i][0]
    if f==a:
        for j in range(len(p[i])):
            print(p[i][j],end=" ")
        print()
#patient above 60
print("patient above age=60")
for i in range(len(p)):
    a=p[i][2]
    if a>=60:
        for j in range(len(p[i])):
            print(p[i][j], end=" ")
        
        print()
    
#with same disease
d=input("enter your disease")
for i in range(len(p)):
    a=p[i][3]
    if d==a:
        
    
        for j in range(len(p[i])):
            print(p[i][j],end=" ")

            
        print()