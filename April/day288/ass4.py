"""

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
"""

n = int(input("Input :"))

isPrime = True

if n < 2:
    isPrime = False
else:
    i = 2
    while n%i==0:
        isPrime = False
        break
    i+=1

if isPrime:
    n = n+1
    i = 2
    while i<n:
        if n%i == 0:
            n = n+1
            break
        i+=1
    else:
       print("Next Prime = ",n)

else:
    n = n-1
    isPrime = False
    for i in range(2,n):
        if n%i==0:
            isPrime = False
            n = n-1      
        else:
            continue
    else:
        if isPrime:
            print("Prev Prime Number = ", n)
        
           



























    