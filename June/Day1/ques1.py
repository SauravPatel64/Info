
"""
1.
 Second Largest Unique Number
Scenario

A sports academy stores athlete scores in a list.

Find the second largest unique score.

Requirements
Read N and list elements from user
Find second largest unique number
If not available, display a message
Test Case

Input:

[10, 20, 30, 40, 40]

Output:

Second Largest = 30

"""


n = int(input("Enter number of elements: "))

nums = []
for i in range(n):
    nums.append(int(input()))

unique_nums = list(set(nums))

if len(unique_nums) < 2:
    print("Second largest unique number not available")
else:
    unique_nums.sort()
    print("Second Largest =", unique_nums[-2])