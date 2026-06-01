

"""
61. Count total alphabets, digits, and special characters.
Input:
S = "a1b!c2"

Output:
Alphabets: 3
Digits: 2
Special: 1
"""

s = input("Enter String : ")

alphabets = 0
digits = 0
special = 0

for i in s:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        digits += 1
    else:
        special += 1

print("Alphabets :", alphabets)
print("Digits :", digits)
print("Special Characters :", special)


"""
62. Count vowels and consonants.
Input:
S = "apple"

Output:
Vowels: 2
Consonants: 3
"""

s = input("Enter String : ")

vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for i in s:
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels :", vowel_count)
print("Consonants :", consonant_count)


"""
63. Count frequency of each character.
Input:
S = "aabcc"

Output:
a: 2
b: 1
c: 2
"""

s = input("Enter String : ")

freq = {}

for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key in freq:
    print(key, ":", freq[key])


"""
64. Count frequency of each vowel.
Input:
S = "programming"

Output:
a: 1
e: 0
i: 1
o: 1
u: 0
"""

s = input("Enter String : ")

vowels = "aeiou"

for v in vowels:
    count = 0

    for ch in s:
        if ch == v:
            count += 1

    print(v, ":", count)


"""
65. Count palindromic substrings.
Input:
S = "aaa"

Output:
6
"""

s = input("Enter String : ")

count = 0

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):

        sub = s[i:j]

        if sub == sub[::-1]:
            count += 1

print("Palindromic Substrings :", count)


"""
66. Count number of sentences in a paragraph.
Input:
P = "This. Is. Test."

Output:
3
"""

p = input("Enter Paragraph : ")

count = 0

for i in p:
    if i == "." or i == "!" or i == "?":
        count += 1

print("Total Sentences :", count)


"""
67. Count how many times a substring appears.
Input:
S = "abab"
Sub = "ab"

Output:
2
"""

s = input("Enter String : ")
sub = input("Enter Substring : ")

count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        count += 1

print("Occurrences :", count)


"""
68. Count the sum of digits present in a string.
Input:
S = "a1b2c3"

Output:
6
"""

s = input("Enter String : ")

total = 0

for i in s:
    if i.isdigit():
        total += int(i)

print("Sum of Digits :", total)


"""
69. Count how many times 'life' appears in a string.
Input:
S = "life is life"

Output:
2
"""

s = input("Enter String : ")

words = s.split()

count = 0

for i in words:
    if i == "life":
        count += 1

print("Count :", count)


"""
70. Compare the number of times 'the' and 'is' appear.
Input:
S = "the cat is on the mat"

Output:
the: 2
is: 1
"""

s = input("Enter String : ")

words = s.split()

the_count = 0
is_count = 0

for i in words:
    if i == "the":
        the_count += 1
    elif i == "is":
        is_count += 1

print("the :", the_count)
print("is :", is_count)


"""
71. Print all substrings.
Input:
S = "abc"

Output:
a
ab
abc
b
bc
c
"""

s = input("Enter String : ")

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])


"""
72. Print all substrings of length n.
Input:
S = "abc"
n = 2

Output:
ab
bc
"""

s = input("Enter String : ")
n = int(input("Enter Length : "))

for i in range(len(s) - n + 1):
    print(s[i:i+n])


"""
73. Find the longest palindromic substring.
Input:
S = "babad"

Output:
bab
"""

s = input("Enter String : ")

longest = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):

        sub = s[i:j]

        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub

print("Longest Palindrome :", longest)


"""
74. Find the longest substring without repeating characters.
Input:
S = "abcabcbb"

Output:
abc
"""

s = input("Enter String : ")

longest = ""

for i in range(len(s)):

    temp = ""

    for j in range(i, len(s)):

        if s[j] not in temp:
            temp += s[j]
        else:
            break

    if len(temp) > len(longest):
        longest = temp

print("Longest Substring :", longest)


"""
75. Find the longest common prefix among strings.
Input:
flower
flow
flight

Output:
fl
"""

strings = input("Enter Strings separated by space : ").split()

prefix = strings[0]

for s in strings[1:]:

    while not s.startswith(prefix):
        prefix = prefix[:-1]

print("Longest Common Prefix :", prefix)


"""
76. Find the longest common suffix among strings.
Input:
baking
making
taking

Output:
king
"""

strings = input("Enter Strings separated by space : ").split()

suffix = strings[0]

for s in strings[1:]:

    while not s.endswith(suffix):
        suffix = suffix[1:]

print("Longest Common Suffix :", suffix)


"""
77. Find the longest substring that appears at both ends.
Input:
S = "abracadabra"

Output:
abra
"""

s = input("Enter String : ")

result = ""

for i in range(1, len(s)):

    sub = s[:i]

    if s.endswith(sub):
        result = sub

print("Longest Matching Substring :", result)


"""
78. Find the longest mirror-image substring at both ends.
Input:
S = "aabccbaa"

Output:
aab
"""

s = input("Enter String : ")

result = ""

for i in range(1, len(s)):

    left = s[:i]
    right = s[len(s)-i:]

    if left == right[::-1]:
        result = left

print("Result :", result)


"""
79. Divide a string into n equal parts.
Input:
S = "abcdef"
n = 3

Output:
ab
cd
ef
"""

s = input("Enter String : ")
n = int(input("Enter Number of Parts : "))

size = len(s) // n

for i in range(0, len(s), size):
    print(s[i:i+size])


"""
80. Print list items containing all characters of a given word.
Input:
List = ["apple", "plea"]
Word = "pal"

Output:
apple
plea
"""

items = input("Enter List Items separated by space : ").split()
word = input("Enter Word : ")

for item in items:

    found = True

    for ch in word:
        if ch not in item:
            found = False
            break

    if found:
        print(item)





```python id="d9qk1m"
"""
81. Generate a hash code or UUID.
Input:
S = "test"

Output:
Hash Code / UUID
"""

import uuid

s = input("Enter String : ")

print("Hash Code :", hash(s))
print("UUID :", uuid.uuid4())


"""
82. Create a string from a character array.
Input:
['h', 'i']

Output:
hi
"""

chars = input("Enter Characters separated by space : ").split()

result = ""

for ch in chars:
    result += ch

print("String :", result)


"""
83. Create a string from a byte array.
Input:
72 101 108

Output:
Hel
"""

bytes_array = list(map(int, input("Enter Byte Values : ").split()))

result = ""

for b in bytes_array:
    result += chr(b)

print("String :", result)


"""
84. Print ASCII value of each character.
Input:
S = "A"

Output:
A : 65
"""

s = input("Enter String : ")

for ch in s:
    print(ch, ":", ord(ch))


"""
85. Convert string into a char array without built-in functions.
Input:
S = "test"

Output:
['t', 'e', 's', 't']
"""

s = input("Enter String : ")

arr = []

for ch in s:
    arr.append(ch)

print(arr)


"""
86. Print all permutations of a string without repetition.
Input:
S = "ab"

Output:
ab
ba
"""

from itertools import permutations

s = input("Enter String : ")

perm = permutations(s)

for p in perm:
    print("".join(p))


"""
87. Print all permutations of a string with repetition.
Input:
S = "aab"

Output:
aab
aba
baa
"""

from itertools import permutations

s = input("Enter String : ")

result = set()

for p in permutations(s):
    result.add("".join(p))

for i in result:
    print(i)


"""
88. Rearrange a string so that identical characters are at least d distance apart.
Input:
S = "aaabc"
d = 2

Output:
abaca
"""

s = input("Enter String : ")

result = ""

used = [False] * len(s)

for i in range(len(s)):
    if not used[i]:
        result += s[i]
        used[i] = True

        for j in range(i + 1, len(s)):
            if s[j] != s[i] and not used[j]:
                result += s[j]
                used[j] = True
                break

for i in range(len(s)):
    if not used[i]:
        result += s[i]

print("Result :", result)


"""
89. Remove 'b' and 'ac' from a string.
Input:
S = "abacbb"

Output:
c
"""

s = input("Enter String : ")

s = s.replace("ac", "")
s = s.replace("b", "")

print("Result :", s)


"""
90. Remove adjacent duplicates recursively.
Input:
S = "azxxzy"

Output:
ay
"""

s = input("Enter String : ")

changed = True

while changed:

    changed = False
    result = ""
    i = 0

    while i < len(s):

        if i < len(s) - 1 and s[i] == s[i + 1]:

            changed = True
            ch = s[i]

            while i < len(s) and s[i] == ch:
                i += 1

        else:
            result += s[i]
            i += 1

    s = result

print("Result :", s)


"""
91. Check if two strings are interleaving of another string.
Input:
S1 = "aab"
S2 = "axy"
S3 = "aaxaby"

Output:
TRUE
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")
s3 = input("Enter Third String : ")

i = j = 0

result = ""

for ch in s3:

    if i < len(s1) and ch == s1[i]:
        result += ch
        i += 1

    elif j < len(s2) and ch == s2[j]:
        result += ch
        j += 1

if result == s3:
    print("TRUE")
else:
    print("FALSE")


"""
92. Check if two strings are pq-balanced.
Input:
S1 = "pqqp"
S2 = "qpqp"

Output:
TRUE
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

p1 = s1.count("p")
q1 = s1.count("q")

p2 = s2.count("p")
q2 = s2.count("q")

if p1 == q1 and p2 == q2:
    print("TRUE")
else:
    print("FALSE")


"""
93. Match strings with wildcard characters (*, ?).
Input:
Pattern = "a?c"
Text = "axc"

Output:
TRUE
"""

import fnmatch

pattern = input("Enter Pattern : ")
text = input("Enter Text : ")

if fnmatch.fnmatch(text, pattern):
    print("TRUE")
else:
    print("FALSE")


"""
94. Find the smallest window containing all characters of another string.
Input:
S1 = "ADOBECODEBANC"
S2 = "ABC"

Output:
BANC
"""

s1 = input("Enter Main String : ")
s2 = input("Enter Pattern String : ")

min_len = len(s1) + 1
result = ""

for i in range(len(s1)):

    temp = ""

    for j in range(i, len(s1)):

        temp += s1[j]

        found = True

        for ch in s2:
            if ch not in temp:
                found = False
                break

        if found:

            if len(temp) < min_len:
                min_len = len(temp)
                result = temp

            break

print("Smallest Window :", result)


"""
95. Find the second most frequent character.
Input:
S = "aabbccdde"

Output:
c or d
"""

s = input("Enter String : ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

values = sorted(set(freq.values()), reverse=True)

if len(values) >= 2:

    second = values[1]

    for key in freq:
        if freq[key] == second:
            print("Second Most Frequent Character :", key)
            break



```python id="x4lf7v"
"""
96. Find the second most frequent word.
Input:
S = "a b a c b"

Output:
c
"""

s = input("Enter String : ")

words = s.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

values = sorted(set(freq.values()), reverse=True)

if len(values) >= 2:

    second = values[1]

    for key in freq:
        if freq[key] == second:
            print("Second Most Frequent Word :", key)
            break


"""
97. Check if two given strings appear at the end of each other (ignoring case).
Input:
S1 = "abc"
S2 = "Xabc"

Output:
TRUE
"""

s1 = input("Enter First String : ").lower()
s2 = input("Enter Second String : ").lower()

if s1.endswith(s2) or s2.endswith(s1):
    print("TRUE")
else:
    print("FALSE")


"""
98. Check if the first 'z' is immediately followed by another 'z'.
Input:
S = "zzyy"

Output:
TRUE
"""

s = input("Enter String : ")

found = False

for i in range(len(s) - 1):

    if s[i] == 'z':

        if s[i + 1] == 'z':
            found = True

        break

print(found)


"""
99. Check if a 'z' is happy (surrounded by same chars).
Input:
S = "azzb"

Output:
FALSE
"""

s = input("Enter String : ")

happy = False

for i in range(1, len(s) - 1):

    if s[i] == 'z':

        if s[i - 1] == 'z' or s[i + 1] == 'z':
            happy = True

        else:
            happy = False
            break

print(happy)



"""
100. Return true if string contains 'abc' not followed by '.'.
Input:
S = "abcx"

Output:
TRUE
"""

s = input("Enter String : ")

found = False

for i in range(len(s) - 2):

    if s[i:i+3] == "abc":

        if i + 3 >= len(s) or s[i + 3] != '.':
            found = True

print(found)


