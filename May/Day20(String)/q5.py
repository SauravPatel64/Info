""" 
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:

```
aabbccdde
```

Output:

```
5
```

"""

s = input("Enter string : ")
newStr = ""
count = 0

for ch in s:
    if ch not in newStr:
        newStr = newStr + ch
        count = count+1
print("Output is : ",count)