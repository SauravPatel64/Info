



patients =  []

def add_patient():
    Id = int(input("Enter Patient Id : "))
    Name = input("Enter Patient Name : ")
    age = int(input("Enter Patient Age : "))
    gender = input("Enter Patient Gender : ")
    disease = input("Enter Patient Disease : ")
    Mobile = int(input("Enter Patient Mobile Number : "))
    
    patient = {}
    
    patient['Patient_ID'] = Id
    patient['Patient_Name'] = Name
    patient['Age'] = age
    patient['Gender'] = gender
    patient['Disease'] = disease
    patient['Mobile_Number'] = Mobile
    
    return patients.append(patient) 

def display_patients():
    for i in patients:
        for key,value in i.items():
            print(key," : ",value)
        
        print()


def search_patients():
    id = int(input("Enter Patient ID : "))
    
    for i in patients:
        if patients[i][0] == id:
            print(patients[i])
            break
    else:
        print("Patient Was not exist  in record")

