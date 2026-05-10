'''
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2

'''
a=int(input("Input :"))
fact=0
s=9

for i in range (1,a+1):
    rem=a%i
    if rem==0:
        fact=fact+1
        if s>i:
            if i==1:
                continue
            s=i
print("Factors Count =",fact)
print("Smallest Factor =",s)