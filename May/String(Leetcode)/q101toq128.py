
```python id="z8kp5m"
"""
101. Check if a string is a valid palindrome ignoring spaces and punctuation.
Input:
S = "A man, a plan, a canal: Panama"

Output:
TRUE
"""

s = input("Enter String : ")

clean = ""

for ch in s:
    if ch.isalnum():
        clean += ch.lower()

if clean == clean[::-1]:
    print("TRUE")
else:
    print("FALSE")


"""
102. Reverse a string using recursion.
Input:
S = "abc"

Output:
cba
"""

def reverse_string(s):

    if len(s) == 0:
        return s

    return reverse_string(s[1:]) + s[0]

s = input("Enter String : ")

print("Reversed String :", reverse_string(s))


"""
103. Check if a string contains balanced parentheses.
Input:
S = "((()))"

Output:
TRUE
"""

s = input("Enter Parentheses String : ")

count = 0
balanced = True

for ch in s:

    if ch == '(':
        count += 1

    elif ch == ')':
        count -= 1

    if count < 0:
        balanced = False
        break

if count != 0:
    balanced = False

print(balanced)


"""
104. Check if a string contains balanced brackets of all types.
Input:
S = "{[()]}"

Output:
TRUE
"""

s = input("Enter Bracket String : ")

stack = []

pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

balanced = True

for ch in s:

    if ch in "({[":
        stack.append(ch)

    elif ch in ")}]":

        if len(stack) == 0 or stack[-1] != pairs[ch]:
            balanced = False
            break

        stack.pop()

if len(stack) != 0:
    balanced = False

print(balanced)


"""
105. Find the longest valid parentheses substring.
Input:
S = "()(())"

Output:
6
"""

s = input("Enter Parentheses String : ")

stack = [-1]

max_len = 0

for i in range(len(s)):

    if s[i] == '(':
        stack.append(i)

    else:
        stack.pop()

        if len(stack) == 0:
            stack.append(i)

        else:
            max_len = max(max_len, i - stack[-1])

print("Longest Length :", max_len)


"""
106. Generate all subsequences of a string.
Input:
S = "ab"

Output:
"", "a", "b", "ab"
"""

def subsequences(s, current, index):

    if index == len(s):
        print(current)
        return

    subsequences(s, current, index + 1)

    subsequences(s, current + s[index], index + 1)

s = input("Enter String : ")

subsequences(s, "", 0)


"""
107. Check if a string is a pangram.
Input:
S = "The quick brown fox jumps over the lazy dog"

Output:
TRUE
"""

s = input("Enter String : ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

found = True

for ch in alphabet:

    if ch not in s:
        found = False
        break

print(found)


"""
108. Check if a string is an isogram.
Input:
S = "ambidextrous"

Output:
TRUE
"""

s = input("Enter String : ").lower()

seen = set()

isogram = True

for ch in s:

    if ch.isalpha():

        if ch in seen:
            isogram = False
            break

        seen.add(ch)

print(isogram)


"""
109. Find the lexicographically smallest substring of length k.
Input:
S = "banana"
k = 3

Output:
ana
"""

s = input("Enter String : ")
k = int(input("Enter k : "))

smallest = s[0:k]

for i in range(len(s) - k + 1):

    sub = s[i:i+k]

    if sub < smallest:
        smallest = sub

print("Smallest Substring :", smallest)


"""
110. Find the lexicographically largest substring of length k.
Input:
S = "banana"
k = 3

Output:
nan
"""

s = input("Enter String : ")
k = int(input("Enter k : "))

largest = s[0:k]

for i in range(len(s) - k + 1):

    sub = s[i:i+k]

    if sub > largest:
        largest = sub

print("Largest Substring :", largest)


"""
111. Check if a string can be rearranged into a palindrome.
Input:
S = "aabbc"

Output:
TRUE
"""

s = input("Enter String : ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

odd = 0

for value in freq.values():

    if value % 2 != 0:
        odd += 1

if odd <= 1:
    print("TRUE")
else:
    print("FALSE")


"""
112. Find the minimum number of deletions to make a string palindrome.
Input:
S = "aebcbda"

Output:
2
"""

s = input("Enter String : ")

rev = s[::-1]

n = len(s)

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):

    for j in range(1, n+1):

        if s[i-1] == rev[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lps = dp[n][n]

print("Minimum Deletions :", n - lps)


"""
113. Find the minimum number of insertions to make a string palindrome.
Input:
S = "aebcbda"

Output:
2
"""

s = input("Enter String : ")

rev = s[::-1]

n = len(s)

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):

    for j in range(1, n+1):

        if s[i-1] == rev[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lps = dp[n][n]

print("Minimum Insertions :", n - lps)
```

```python id="t2yq8w"
"""
114. Check if one string is a subsequence of another.
Input:
S1 = "ace"
S2 = "abcde"

Output:
TRUE
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

i = 0

for ch in s2:

    if i < len(s1) and ch == s1[i]:
        i += 1

if i == len(s1):
    print("TRUE")
else:
    print("FALSE")


"""
115. Find the edit distance (Levenshtein distance) between two strings.
Input:
S1 = "kitten"
S2 = "sitting"

Output:
3
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

m = len(s1)
n = len(s2)

dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(m+1):
    dp[i][0] = i

for j in range(n+1):
    dp[0][j] = j

for i in range(1, m+1):

    for j in range(1, n+1):

        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]

        else:
            dp[i][j] = 1 + min(
                dp[i-1][j],
                dp[i][j-1],
                dp[i-1][j-1]
            )

print("Edit Distance :", dp[m][n])


"""
116. Check if a string is a valid shuffle of two other strings.
Input:
S1 = "xy"
S2 = "12"
S3 = "x1y2"

Output:
TRUE
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")
s3 = input("Enter Third String : ")

temp = s1 + s2

if sorted(temp) == sorted(s3):
    print("TRUE")
else:
    print("FALSE")


"""
117. Check if a string contains duplicate substrings.
Input:
S = "ababa"

Output:
TRUE
"""

s = input("Enter String : ")

found = False

for i in range(len(s)):

    for j in range(i + 1, len(s) + 1):

        sub = s[i:j]

        if s.count(sub) > 1:
            found = True
            break

    if found:
        break

print(found)


"""
118. Find the longest repeated substring.
Input:
S = "banana"

Output:
ana
"""

s = input("Enter String : ")

longest = ""

for i in range(len(s)):

    for j in range(i + 1, len(s) + 1):

        sub = s[i:j]

        if s.count(sub) > 1 and len(sub) > len(longest):
            longest = sub

print("Longest Repeated Substring :", longest)


"""
119. Find the smallest substring containing all vowels.
Input:
S = "aeiouy"

Output:
aeiou
"""

s = input("Enter String : ")

vowels = "aeiou"

smallest = ""

for i in range(len(s)):

    temp = ""

    for j in range(i, len(s)):

        temp += s[j]

        found = True

        for v in vowels:

            if v not in temp:
                found = False
                break

        if found:

            if smallest == "" or len(temp) < len(smallest):
                smallest = temp

            break

print("Smallest Substring :", smallest)


"""
120. Find the longest substring containing only vowels.
Input:
S = "abaeiouy"

Output:
aeiou
"""

s = input("Enter String : ")

vowels = "aeiouAEIOU"

longest = ""
temp = ""

for ch in s:

    if ch in vowels:
        temp += ch

        if len(temp) > len(longest):
            longest = temp

    else:
        temp = ""

print("Longest Vowel Substring :", longest)


"""
121. Check if a string contains only binary digits (0/1).
Input:
S = "1010"

Output:
TRUE
"""

s = input("Enter Binary String : ")

binary = True

for ch in s:

    if ch not in "01":
        binary = False
        break

print(binary)


"""
122. Convert a binary string to decimal.
Input:
S = "101"

Output:
5
"""

binary = input("Enter Binary String : ")

decimal = 0
power = 0

for ch in binary[::-1]:

    decimal += int(ch) * (2 ** power)

    power += 1

print("Decimal :", decimal)


"""
123. Convert a decimal number to binary string.
Input:
N = 5

Output:
101
"""

n = int(input("Enter Number : "))

binary = ""

while n > 0:

    binary = str(n % 2) + binary

    n = n // 2

print("Binary :", binary)
```

```python id="q7vc4r"
"""
124. Find the longest common subsequence of two strings.
Input:
S1 = "AGGTAB"
S2 = "GXTXAYB"

Output:
GTAB
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

m = len(s1)
n = len(s2)

dp = [[""]*(n+1) for _ in range(m+1)]

for i in range(m):

    for j in range(n):

        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + s1[i]

        else:

            if len(dp[i][j+1]) > len(dp[i+1][j]):
                dp[i+1][j+1] = dp[i][j+1]

            else:
                dp[i+1][j+1] = dp[i+1][j]

print("LCS :", dp[m][n])


"""
125. Find the shortest common supersequence of two strings.
Input:
S1 = "AGGTAB"
S2 = "GXTXAYB"

Output:
AGGXTXAYB
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

i = 0
j = 0

result = ""

while i < len(s1) and j < len(s2):

    if s1[i] == s2[j]:
        result += s1[i]
        i += 1
        j += 1

    else:
        result += s1[i]
        i += 1

result += s1[i:]
result += s2[j:]

print("Shortest Common Supersequence :", result)


"""
126. Print all anagrams of a string.
Input:
S = "cat"

Output:
cat
cta
act
atc
tca
tac
"""

from itertools import permutations

s = input("Enter String : ")

perm = permutations(s)

for p in perm:
    print("".join(p))


"""
127. Group words that are anagrams from an array of strings.
Input:
eat tea tan ate nat

Output:
[['eat', 'tea', 'ate'], ['tan', 'nat']]
"""

words = input("Enter Words : ").split()

groups = {}

for word in words:

    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))


"""
128. Check if a string follows a given pattern.
Input:
Pattern = "abba"
S = "dog cat cat dog"

Output:
TRUE
"""

pattern = input("Enter Pattern : ")
s = input("Enter Words : ").split()

if len(pattern) != len(s):
    print("FALSE")

else:

    mapping = {}
    used = {}

    valid = True

    for i in range(len(pattern)):

        p = pattern[i]
        word = s[i]

        if p in mapping:

            if mapping[p] != word:
                valid = False
                break

        else:

            if word in used:
                valid = False
                break

            mapping[p] = word
            used[word] = True

    print(valid)

