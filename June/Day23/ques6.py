"""  
6.
 Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.

Input
Enter Coupon Number:
29
Output
Prime Number

"""

n = int(input("Enter Coupon Number: "))

def prime(n, divisor):
    
    if n <= 1:
        return False
    if divisor == 1:
        return True
    
    if n % divisor == 0:
        return False
        
    return prime(n, divisor - 1)



if prime(n, n - 1):
    print("Output: Prime Number")
else:
    print("Output: Not a Prime Number")
