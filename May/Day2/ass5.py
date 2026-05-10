"""
5. Digit Alternating Sum System

A coding system calculates alternating sum of digits (add, subtract, add...).

Write a program to:

Traverse digits from left to right
Add first digit, subtract second, add third, and so on
Display final alternating sum
If result is positive → print Positive Pattern
Else → print Negative Pattern

Input:
1234

Output:
Result = -2
Negative Pattern

Input:
8642

Output:
Result = 8
Positive Pattern
"""

num = int(input("Input =  "))

n = 0
while num > 0:
    last = num % 10
    n = n * 10 + last
    num = num // 10

i = 1
total = 0  

while n > 0:
    last = n % 10

    if i % 2 != 0:  
        total += last
    else:            
        total -= last

    i += 1
    n = n // 10

print(f"Result = {total}")

if total > 0:
    print("Positive Pattern")
else:
    print("Negative Pattern")    
    
