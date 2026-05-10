"""
4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number
"""

num = input("Input : ")
len = len(num)

n = int(num)
maxDiff = 0
rev =  0
count = 0
allDiff = 0
while n>0:
    last = n%10
    rev = rev*10 + last
    n = n//10

print("Differences : ",end=" ")

while rev>9:
    last = rev%10 
    secLast = (rev//10)%10
    diff = abs(last - secLast)
    print(diff,end=" ")
    
    if diff>2:
        count+=1
    if maxDiff < diff:
        maxDiff = diff

    if diff<= 2:
        allDiff+=1

    rev = rev//10

print()
print(f"Count (>2) = {count}")
print(f"Max Difference = {maxDiff}")
if allDiff == len:
    print("Smooth Number")
else:
    print("Smooth Number")













    
    