"""
10. Military Recruitment Fitness System

Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.

If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.

If age is above 30 or below 18, not eligible.

Input:
Age = 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected
"""

age = int(input("Age = "))
bmi = int(input("BMI = "))
running_time = int(input("Running Time = "))
medical = input("Medical = ").lower()

if 18 <= age <= 25:
    if 18 <= bmi <= 25:
        if running_time <= 15:
            if medical == "fit":
                status = "Selected"
            else:
                status = "Medical Reject"
        else:
            status = "Physical Fail"
    else:
        status = "BMI Fail"

elif 26 <= age <= 30:
    if running_time <= 14 and medical.lower() == "fit":
        status = "Conditional Selection"
    else:
        status = "Reject"

else:
    status = "Not Eligible"


print(f"Selection Status = {status}")