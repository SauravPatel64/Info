"""

4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected 
"""

num = int(input("Input = "))
n=0
while num>0:
    last = num%10
    n = n*10 + last
    num = num//10


first = n%10
lastSec = n//10
second = lastSec%10

gap =  abs(second - first)

while n>9:
    fir = n%10
    lastSec = n//10
    sec = lastSec%10 
    digitGap = abs(fir-sec)
    if digitGap == gap:
        n = n//10
    else:
        print(f"Initial Gap = {gap}")
        print("Pattern Break Detected")
        break

else:
    print(f"Initial Gap = {gap}")
    print("Consistent Pattern")





