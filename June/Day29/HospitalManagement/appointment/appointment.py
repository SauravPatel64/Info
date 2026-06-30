

appointments = []

def book_appointment():
    ID = int(input("Enter appointment ID : "))
    Patient_ID = int(input("Enter Patient ID : "))
    Doctor_ID = int(input("Enter Doctor ID : "))
    Date = input("Enter appointment Date dd/mm/yrs : ")
    time = input("Enter appointment time hh-mm-ss : ")
    
    appointment  = {}
    
    appointment['Appointment ID'] = ID
    appointment['Patient ID'] = Patient_ID
    appointment['Doctor ID'] = Doctor_ID
    appointment['Appointment Date'] = Date
    appointment['Appointment Time'] = time
    
    return appointments.append(appointment)


def show_appointments():
    for i in appointments:
        for key,value in i.items():
            print(f"{key} : {value}")
            
        print()
 
 