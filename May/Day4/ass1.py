"""
1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern
"""

num  = int(input("Input : "))
n = 0
maxdiff = 0
alldiff = 0
a=""

len = len(str(num))-1
count = 0
print("Difference : ",end = " ")
while num>0:
    last = num%10
    n = n*10 + last
    num = num//10

last = n%10
seclast = (n//10)%10
diff = abs(seclast - last)

alldiff = diff
uni = 0
while n>9:
    last = n%10
    seclast = (n//10)%10
    diff = abs(seclast - last)
    print(diff,end=" ")

    if maxdiff < diff:
        maxdiff = diff
    if alldiff == diff:
        uni = uni+1
        
    if diff %2==0:
        count+=1
    
    n = n//10

print()
print(f"Even Differences Count = {count}")
print(f"Max Difference = {maxdiff}")
if uni == len:
    print("Uniform Pattern")
else:
    print("Non- Uniform Pattern")
        
    
    
    