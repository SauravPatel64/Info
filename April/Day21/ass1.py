"""
1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation

"""

age = int(input("Policy Age =  "))
amt = int(input("Claim Amount = "))
accident = input("Accident Type = ").lower()

if  age >= 2:
    if amt<= 50000:
        if accident == "minor":
            print("Approved the claim")
        else:
            print("Approved with Investigation")
    elif amt >= 50001 and  amt<=200000:
        if accident == "major":
            print("Approved with Investigation")
        else:
            print("reject")
    else:
        print("reject")

elif age < 2:
    if accident == "minor":
        print("reject")
    else:
        print("pending review")








        