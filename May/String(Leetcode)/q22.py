""" 
Print all characters that occur exactly twice. S = "aabbcdee" b', 'e
"""

s = input("Enter String : ")

seen = []
for char in s:
    if char not in seen:
        seen.append(char)

for char in seen:
    count = 0
    for item in s:
        if item == char:
            count += 1
    if count == 2:
        print(char)
