"""  
Check if all characters in a string are unique. S1 = "abc", S2 = "abca" S1: True, S2: False
"""

s = input("Enter String : ")

seen = []
is_unique = True

for char in s:
    if char in seen:
        is_unique = False
        break
    seen.append(char)

print(is_unique)

