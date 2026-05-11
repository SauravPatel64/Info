"""
    3)	WAP to find out all the leap years between two entered years
"""

first = int(input("Enter Starting Year =  "))
second = int(input("Enter Second Year = "))

for i in range(first, second):
    if (i%4==0 and i%100!=0) or (i%400==0):
        print(i)
        
    