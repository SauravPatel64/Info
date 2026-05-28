

```python id="n7zq2a"
"""
1. Find the length of a string.
Input:
S = "programming"

Output:
11
"""

s = input("Enter String : ")

count = 0

for i in s:
    count += 1

print("Length :", count)


"""
2. Copy one string to another.
Input:
S1 = "source"

Output:
S2 = "source"
"""

s1 = input("Enter String : ")

s2 = ""

for ch in s1:
    s2 += ch

print("Copied String :", s2)


"""
3. Concatenate two strings.
Input:
S1 = "Hello"
S2 = "World"

Output:
HelloWorld
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

result = s1 + s2

print("Concatenated String :", result)


"""
4. Compare two strings (case-sensitive).
Input:
S1 = "Test"
S2 = "test"

Output:
Not Equal
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

if s1 == s2:
    print("Equal")
else:
    print("Not Equal")


"""
5. Compare two strings ignoring case.
Input:
S1 = "Test"
S2 = "test"

Output:
Equal
"""

s1 = input("Enter First String : ").lower()
s2 = input("Enter Second String : ").lower()

if s1 == s2:
    print("Equal")
else:
    print("Not Equal")


"""
6. Convert a string to uppercase.
Input:
S = "hello"

Output:
HELLO
"""

s = input("Enter String : ")

print("Uppercase :", s.upper())


"""
7. Convert a string to lowercase.
Input:
S = "HELLO"

Output:
hello
"""

s = input("Enter String : ")

print("Lowercase :", s.lower())


"""
8. Toggle the case of each character.
Input:
S = "MiXED"

Output:
mIxed
"""

s = input("Enter String : ")

result = ""

for ch in s:

    if ch.isupper():
        result += ch.lower()

    elif ch.islower():
        result += ch.upper()

    else:
        result += ch

print("Toggled String :", result)


"""
9. Check whether a string is empty.
Input:
S1 = ""
S2 = "A"

Output:
True / False
"""

s = input("Enter String : ")

if s == "":
    print("True")
else:
    print("False")


"""
10. Trim leading, trailing, or extra spaces.
Input:
S = "  hello  world  "

Output:
hello world
"""

s = input("Enter String : ")

words = s.split()

result = " ".join(words)

print("Trimmed String :", result)


"""
11. Get the character at a given index.
Input:
S = "Python"
Index = 2

Output:
t
"""

s = input("Enter String : ")
index = int(input("Enter Index : "))

print("Character :", s[index])


"""
12. Get the Unicode code point of a character at index.
Input:
S = "A"
Index = 0

Output:
65
"""

s = input("Enter String : ")
index = int(input("Enter Index : "))

print("Unicode :", ord(s[index]))


"""
13. Get the Unicode code point before index.
Input:
S = "Hello"
Index = 1

Output:
72
"""

s = input("Enter String : ")
index = int(input("Enter Index : "))

print("Unicode Before Index :", ord(s[index - 1]))


"""
14. Find the first occurrence of a character.
Input:
S = "banana"
Char = 'a'

Output:
1
"""

s = input("Enter String : ")
ch = input("Enter Character : ")

index = -1

for i in range(len(s)):

    if s[i] == ch:
        index = i
        break

print("First Occurrence :", index)


"""
15. Find the last occurrence of a character.
Input:
S = "banana"
Char = 'a'

Output:
5
"""

s = input("Enter String : ")
ch = input("Enter Character : ")

index = -1

for i in range(len(s)):

    if s[i] == ch:
        index = i

print("Last Occurrence :", index)


"""
16. Count total occurrences of a character.
Input:
S = "programming"
Char = 'g'

Output:
2
"""

s = input("Enter String : ")
ch = input("Enter Character : ")

count = 0

for i in s:

    if i == ch:
        count += 1

print("Total Occurrences :", count)
