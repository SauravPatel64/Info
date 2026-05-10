"""
3.

Fibonacci Population Growth Tracker

A wildlife research team is studying the growth of a rare species.  
They observe that the population follows a Fibonacci pattern:

- Month 1 → 0 animals  
- Month 2 → 1 animal  
- Every next month → sum of previous two months  

The researchers want to analyze the growth pattern.

Write a program to:

- Read number of months n
- Generate Fibonacci series up to n months using loop
- Print population for each month
- Find total population observed
- Count how many months population exceeded 5

Input:
8

Output:
Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2

"""

n = int(input("Enter the number = "))

first = 0
second = 1
print(first)
print(second)
sum = first + second
p = 0
greater = 0
i = 3

while i<=n:
    next = first + second
    print(next)
    sum += next
    first = second
    second = next
    p = next
    if p>5:
        greater += 1
    i+=1

print(f"Total Population = {sum}")
print(f"Months with Population > 5 = {greater}")



















