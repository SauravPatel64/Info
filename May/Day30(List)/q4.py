""" 
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3

"""

n = int(input())
elements = list(map(int, input().split()))

if not elements:
    print("Longest Consecutive Length = 0")
else:
    elements.sort()
    
    longest_streak = 1
    current_streak = 1
    
    for i in range(1, len(elements)):
        if elements[i] != elements[i - 1]:
            if elements[i] == elements[i - 1] + 1:
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = 1
                
    if current_streak > longest_streak:
        longest_streak = current_streak
        
    print(f"Longest Consecutive Length = {longest_streak}")
