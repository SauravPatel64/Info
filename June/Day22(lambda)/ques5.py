""" 
Assignment 1: Smart Street Lights (Fibonacci Series)

A smart city installs street lights in a newly developed area. The number of lights installed each month follows the Fibonacci pattern.

Month 1 → 0 lights
Month 2 → 1 light
Every following month, the number of lights installed is the sum of the previous two months.

As a software developer, your task is to help the city planning department generate the installation schedule.

Task

Write a recursive function to print the first N Fibonacci numbers.

Input
Enter the number of months:
7
Output
0 1 1 2 3 5 8
"""

m = int(input("Enter the number of months: "))
n1 = 0
n2 = 1

fib = [0, 1] 

def light(n):
    global n1, n2  
    if n <= 2:     
        return 0
    
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    fib.append(n3)
    return light(n - 1)

light(m)

print(*(fib[:m]))
