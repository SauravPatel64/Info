
# import patient, appointment, billing, doctor
from patient import display_patients, add_patient, search_patients
from appointment import book_appointment,show_appointments
from doctor import add_doctor, display_doctors
from billing import generate_bill 





print("""========== Hospital Management System ==========

1. Add Patient
2. Display Patients
3. Search Patient
4. Add Doctor
5. Display Doctors
6. Book Appointment
7. Show Appointments
8. Generate Bill
9. Exit

According to user choice call the required functions from packages.

--------------------------------------------------""")

while True:
    a = int(input("Enter Case No: "))
    
    match a:
        case 1:
            print()
            add_patient()
            print("--------------------------------------------------")
        case 2:
            print()
            display_patients()
            print("--------------------------------------------------")
            
        case 3:
            print()
            search_patients()
            print("--------------------------------------------------")
            
        case 4:
            print()
            add_doctor()
            print("--------------------------------------------------")
            
        case 5:
            print()
            display_doctors()
            print("--------------------------------------------------")
            
        case 6:
            print()
            book_appointment()
            print("--------------------------------------------------")
            
        case 7:
            print()
            show_appointments()
            print("--------------------------------------------------")
            
        case 8:
            print()
            generate_bill()
            print("--------------------------------------------------")
            
        case 9: 
            break
    
    

