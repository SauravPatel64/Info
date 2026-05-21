""" 
1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc
"""

s= input("Enter String : ")
curr_str = ""
long_str = ""

for ch in s:
    if ch in curr_str:
        pos = 0
        for i in range(len(curr_str)):
            pos = i
            break
    
        curr_str = curr_str[pos+1:]
    
    curr_str = curr_str + ch
    
    if len(curr_str)> len(long_str):
        long_str = curr_str

print(long_str)
            
