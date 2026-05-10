'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''

a=int(input("Input : "))
lar=0
sml=9
x=0

while a>0:
    rem=a%10
    if lar<rem:
        lar=rem
    elif sml>rem:
        sml=rem
    a=a//10
print("Largest =",lar)
print("Smallest =",sml)

sum=lar+sml
print("Sum =",sum)

for i in range (2,sum//2+1):
    if sum%i==0:
        x=1
        break
if x==1:
    print("Not Prime")
else:
    print("Prime")

