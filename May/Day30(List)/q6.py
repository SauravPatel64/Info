""" 
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]


"""
n = int(input())
elements = list(map(int, input().split()))

result = []

for i in range(len(elements)):
    product = 1
    for j in range(len(elements)):
        if i != j:
            product *= elements[j]
    result.append(product)

print(result)
