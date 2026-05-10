'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''

a=int(input("Input :"))

for i in range (1,a//2+1):
    c=True
    if a%i==0: 
        if i==1:
            continue
        c=False
        break
if c:
    print("Prime")
else:
    print("Not Prime")

if c:
    g=a+1
    while True:
   
        d=0
        for i in range(2,g//2+1):
            if g%i==0:
                d=1
                break
        if d==0:
            print("Next Prime =",g)
            break
        g=g+1
else:
    g=a-1
    while True:
   
        d=0
        for i in range(2,g//2+1,1):
            if g%i==0:
                d=1
                break
        if d==0:
            print("Previous Prime =",g)
            break
        g=g+-1
    