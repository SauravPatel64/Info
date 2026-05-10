'''
1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number'''

a=int(input("Input :"))
count=0
for i in range (1,a+1):
    if a%i==0:
        count=count+1
if count==2:
    print("Prime Number")
else :
    print("Not Prime Number")