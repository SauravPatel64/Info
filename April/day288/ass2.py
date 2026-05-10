"""

2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17

"""

n = int(input("Input : "))

if n <2:
    print("Next Prime = 2")

i = 2

while i<n:
    n = n+1
    isPrime = True
    
    