"""
5.
Strong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145
"""


x = int(input("Enter starting number: "))
y = int(input("Enter ending number: "))

print("Strong Numbers are: ")
for i in range(x,y+1):
    num = i
    sum = 0
    
    while num>0:
        last = num%10
        fact = 1
        for j in range(1, last+1):
                fact =  fact*j
        sum = sum+fact
        num = num//10

    if sum == i:
        print(i)





