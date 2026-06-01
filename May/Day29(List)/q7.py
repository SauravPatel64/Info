""" 

7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3
"""

elements = list(map(int, input().strip('[]').replace(',', ' ').split()))

factorials = []

for num in elements:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    factorials.append(fact)

fact_sum = sum(factorials)

if factorials:
    fact_max = max(factorials)
else:
    fact_max = 0

even_count = 0
for fact in factorials:
    if fact % 2 == 0:
        even_count += 1

print(factorials)
print(f"Sum = {fact_sum}")
print(f"Max = {fact_max}")
print(f"Even Count = {even_count}")
