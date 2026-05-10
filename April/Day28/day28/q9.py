'''
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''

a=int(input("Input : "))
even=0
odd=0
count=0


while a>0:
    rem=a%10
    if rem%2==0:
        even=even+1
    elif rem%2!=0:
        odd=odd+1
    a=a//10


c=abs(even-odd)
print("Even =",even)
print("Odd =",odd)
print("Difference =",c)


for i in range (1,c+1):
    rem=c%i
    if rem==0:
        count=count+1
if count==2:
    print("Prime")
else :
    print("Not Prime")