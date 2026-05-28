""" 
21). Find the first non-repeating character. S = "aabbcde" c

"""

s = input("Enter String : ")

seen = []
repeated = []

for char in s:
    if char in seen:
        if char not in repeated:
            repeated.append(char)
    else:
        seen.append(char)

result = ""
for char in s:
    if char not in repeated:
        result = char
        break

print(result)


