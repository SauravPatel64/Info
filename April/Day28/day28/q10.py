'''
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''


a=int(input("Input :"))
count=0
sum=0
c=9
x=0

while a>0:
    rem=a%10
    if rem==0:
        count=count+1
    sum=sum+rem
    if rem<c:
        c=rem
    a=a//10
f=sum*c
print("Zero Count =",count)
print("Sum =",sum)
print("Smallest Digit =",c)  
print("Final Result =",f)

for i in range (1,f+1):
    if f%i==0:
        x=x+1
if x==2:
    print("Prime Number ")
else :
    print("Not Prime")


  