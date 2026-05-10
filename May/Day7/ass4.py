"""
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
"""

x = int(input("Enter starting number: "))
y = int(input("Enter ending number: "))

for i in range(x,y+1):
    temp = i
    num= 0
    while temp>0:
        last = temp%10
        num = num + last**3
        temp = temp//10
    if num == i:
        print(i)