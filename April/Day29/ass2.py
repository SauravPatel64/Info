"""
2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
=======
"""
n=int(input("Input:"))

sum=0
i=1
count=0
product=1
while n>0:
    a=n%10
    sum=sum+a
    product=product*a
    difference=product-sum
    i=1
    while difference>0:
        digit=difference%10
        count=count+digit
        i+=1
        difference=difference//10
    f=difference+count
    i+=1
    n=n//10
print("Sum =",sum)
print("Product =",product)
print("Difference =",difference)
print("Digit =",digit)
print("Final result =",f)

if f<=1:
    print ("Not prime")
else:
    while i>0:
        if f%i==0:
            print("Not prime")
        i+=1
    else:
        print("Prime")

