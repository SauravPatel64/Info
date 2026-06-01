""" 
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found

"""

n = int(input())
elements = list(map(int, input().split()))

found = False

for num in elements:
    if elements.count(num) > n / 2:
        print(f"Majority Element = {num}")
        found = True
        break

if not found:
    print("No Majority Element Found")
