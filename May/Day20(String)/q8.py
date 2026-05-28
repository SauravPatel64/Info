
"""  

8.
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not foundp
"""
text = "aaabbbbccddeee"

cleaned_text = ""

for char in text:
    if char != " ":
        if "A" <= char <= "Z":
            cleaned_text += chr(ord(char) + 32)
        else:
            cleaned_text += char

counts = {}
for char in cleaned_text:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

highest_freq = 0
second_highest_freq = 0

for freq in counts.values():
    if freq > highest_freq:
        second_highest_freq = highest_freq
        highest_freq = freq
    elif freq < highest_freq and freq > second_highest_freq:
        second_highest_freq = freq

if second_highest_freq == 0:
    print("Second highest repeating character not found")
else:
    for char, freq in counts.items():
        if freq == second_highest_freq:
            print(char)
            break
