


Doctors =  []

def add_doctor():
    id = int(input("Enter Doctor ID : "))
    name = input("Enter Doctor Name : ")
    domain = input("Enter Doctor Specialization : ")
    exp = input("Enter Doctor Experience : ")
    fees = int(input("Enter Doctor Fee : "))
    
    doctor = {}
    
    doctor['Doctor ID'] = id
    doctor['Doctor Name'] = name
    doctor['Specialization'] =  domain
    doctor['Experience'] = exp
    doctor['Consultation Fees'] = fees
    
    return Doctors.append(doctor)


def display_doctors():
    for i in Doctors:
        for key,value in i.items():
            print(f"{key} : {value}")

        