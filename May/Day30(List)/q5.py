""" 
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found

"""

n = int(input())
elements = list(map(int, input().split()))

total_sum = sum(elements)
left_sum = 0
found = False

for i in range(len(elements)):
    right_sum = total_sum - left_sum - elements[i]
    
    if left_sum == right_sum:
        print(f"Equilibrium Index = {i}")
        found = True
        break
        
    left_sum += elements[i]

if not found:
    print("No Equilibrium Index Found")
