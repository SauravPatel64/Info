


def generate_bill():
    id = int(input("Enter Patient ID : "))
    charge = int(input("Enter Consultation Charges : "))
    cost = int(input("Enter Medicine Cost : "))
    test_charge = int(input("Enter Test CHarges : "))
    
    total = charge + cost + test_charge
    print(f'Total Bill = {total}')
    
    