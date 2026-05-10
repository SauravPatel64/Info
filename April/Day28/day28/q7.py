'''
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''

a=int(input("Input :"))
sum=0
x=0

while a>0:
    rem=a%10
    sum=sum+rem
    a=a//10

print("Sum =",sum)

for i in range (2,sum//2+1):
    if sum%i==0:
        x=1
        break
if x==1:
    print("Not a Lucky Number")
else :
    print("Lucky NUmber")
