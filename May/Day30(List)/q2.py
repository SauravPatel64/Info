""" 
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found

---
"""

# Read the number of elements
n = int(input("Enter total number of IDs (N): "))

# Read the list elements
emp_ids = list(map(int, input().split()))

# Variable to track if a repeating number is found
found = False

# Loop through the list to find the first repeating number
for i in range(len(emp_ids)):
    # Check if the current number appears again later in the list
    if emp_ids[i] in emp_ids[i + 1:]:
        print(f"First Repeating Number = {emp_ids[i]}")
        found = True
        break  # Exit immediately on the first match

# If the loop completes without finding any repetition
if not found:
    print("No Repeating Number Found")








""" 