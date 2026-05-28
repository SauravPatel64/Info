
""" 
## 25. Count total words in a string

**Question:** Count total words in a string.
Input: `S = "This is a test"`
Output: `4`

"""
s = input("Enter String : ")

words = s.split()

print("Total Words :", len(words))

"""

## 26. Find the first occurrence of a word

**Question:** Find the first occurrence of a word.
Input: `S = "Test this test", Word = "test"`
Output: `10`
"""
s = input("Enter String : ")
word = input("Enter Word : ")

index = s.lower().find(word.lower())

print("First Occurrence Index :", index)

"""

## 27. Find the last occurrence of a word

**Question:** Find the last occurrence of a word.
Input: `S = "Test this test", Word = "test"`
Output: `10`

"""
s = input("Enter String : ")
word = input("Enter Word : ")

index = s.lower().rfind(word.lower())

print("Last Occurrence Index :", index)

"""
## 28. Count occurrences of a word

**Question:** Count occurrences of a word.
Input: `S = "word word other word", Word = "word"`
Output: `3`

"""
s = input("Enter String : ")
word = input("Enter Word : ")

words = s.split()

count = 0

for i in words:
    if i == word:
        count += 1

print("Occurrences :", count)

"""
## 29. Remove occurrences of a word

**Question:** Remove occurrences of a word.
Input: `S = "a test b test c", Word = "test"`
Output: `"a b c"`

"""
s = input("Enter String : ")
word = input("Enter Word to Remove : ")

words = s.split()

result = []

for i in words:
    if i != word:
        result.append(i)

print("Result :", " ".join(result))

"""
## 30. Replace a word with another word

**Question:** Replace a word with another word.
Input: `S = "old data", Old="old", New="new"`
Output: `"new data"`

"""
s = input("Enter String : ")
old = input("Enter Old Word : ")
new = input("Enter New Word : ")

words = s.split()

for i in range(len(words)):
    if words[i] == old:
        words[i] = new

print("Result :", " ".join(words))

"""

## 31. Remove duplicate words

**Question:** Remove duplicate words.
Input: `S = "the cat and the dog"`
Output: `"the cat and dog"`
"""

s = input("Enter String : ")

words = s.split()

result = []

for i in words:
    if i not in result:
        result.append(i)

print("Result :", " ".join(result))

"""

## 32. Count frequency of each word

**Question:** Count frequency of each word.
Input: `S = "apple banana apple"`
Output: `apple: 2, banana: 1`

"""
s = input("Enter String : ")

words = s.split()

freq = {}

for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key in freq:
    print(key, ":", freq[key])

"""
## 33. Find the longest word

**Question:** Find the longest word.
Input: `S = "find the longest word"`
Output: `"longest"`

"""

s = input("Enter String : ")

words = s.split()

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest Word :", longest)

"""
## 34. Find the shortest word

**Question:** Find the shortest word.
Input: `S = "find the shortest word"`
Output: `"the"`

"""

s = input("Enter String : ")

words = s.split()

shortest = words[0]

for i in words:
    if len(i) < len(shortest):
        shortest = i

print("Shortest Word :", shortest)

"""

## 35. Find the first palindrome word

**Question:** Find the first palindrome word.
Input: `S = "this madam is here"`
Output: `"madam"`

"""

s = input("Enter String : ")

words = s.split()

for i in words:
    if i == i[::-1]:
        print("First Palindrome Word :", i)
        break

"""

## 36. Reverse order of words

**Question:** Reverse order of words.
Input: `S = "one two three"`
Output: `"three two one"`

"""

s = input("Enter String : ")

words = s.split()

words.reverse()

print("Result :", " ".join(words))

"""

## 37. Reverse each word

**Question:** Reverse each word.
Input: `S = "cat dog"`
Output: `"tac god"`

"""

s = input("Enter String : ")

words = s.split()

result = []

for i in words:
    result.append(i[::-1])

print("Result :", " ".join(result))

"""

## 38. Reverse words without split()

**Question:** Reverse words without split().
Input: `S = "a b c"`
Output: `"c b a"`

"""

s = input("Enter String : ")

word = ""
result = []

for i in s:
    if i != " ":
        word += i
    else:
        result.insert(0, word)
        word = ""

result.insert(0, word)

print("Result :", " ".join(result))

"""

## 39. Search all occurrences of a character

**Question:** Search all occurrences of a character.
Input: `S = "banana", Char='a'`
Output: `1, 3, 5`

"""

s = input("Enter String : ")
ch = input("Enter Character : ")

for i in range(len(s)):
    if s[i] == ch:
        print(i, end=" ")

"""

## 40. Search all occurrences of a word

**Question:** Search all occurrences of a word.
Input: `S = "a b a b", Word='b'`
Output: `2, 6`

"""
s = input("Enter String : ")
word = input("Enter Word : ")

index = 0

while True:
    pos = s.find(word, index)

    if pos == -1:
        break

    print(pos, end=" ")

    index = pos + 1

"""

## 41. Check if a string contains a substring (without using built-in method)

**Question:** Check if a string contains a substring.
Input: `S1 = "Hello", Sub="ell"`
Output: `TRUE`

"""
s = input("Enter Main String : ")
sub = input("Enter Substring : ")

found = False

for i in range(len(s) - len(sub) + 1):

    match = True

    for j in range(len(sub)):
        if s[i + j] != sub[j]:
            match = False
            break

    if match:
        found = True
        break

if found:
    print("TRUE")
else:
    print("FALSE")

"""

## 42. Check if two strings are equal without equals()

**Question:** Check if two strings are equal without equals().
Input: `S1 = "abc", S2 = "abc"`
Output: `TRUE`

"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

if len(s1) != len(s2):
    print("FALSE")
else:
    same = True

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            same = False
            break

    if same:
        print("TRUE")
    else:
        print("FALSE")

"""

## 43. Check if two strings are rotations of each other

**Question:** Check if two strings are rotations of each other.
Input: `S1 = "abcde", S2 = "cdeab"`
Output: `TRUE`

"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("TRUE")
else:
    print("FALSE")

"""

## 44. Check if two strings are anagrams

**Question:** Check if two strings are anagrams.
Input: `S1 = "listen", S2 = "silent"`
Output: `TRUE`

"""
s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

if sorted(s1) == sorted(s2):
    print("TRUE")
else:
    print("FALSE")

"""

## 45. Check whether a string starts/ends with another string

**Question:** Check whether a string starts/ends with another string.
Input: `S = "apple pie", Prefix = "apple", Suffix = "pie"`
Output: `Start: True, End: True`

"""

s = input("Enter String : ")
prefix = input("Enter Prefix : ")
suffix = input("Enter Suffix : ")

start = s.startswith(prefix)
end = s.endswith(suffix)

print("Start :", start)
print("End :", end)

"""

## 46. Check if a substring appears at both the start and end

**Question:** Check if a substring appears at both the start and end.
Input: `S = "abcabca", Sub="abca"`
Output: `TRUE`

"""

s = input("Enter String : ")
sub = input("Enter Substring : ")

if s.startswith(sub) and s.endswith(sub):
    print("TRUE")
else:
    print("FALSE")


"""
47. Check for substring using concatenation trick.
Input:
S1 = "CDAB"
S2 = "ABCD"

Output:
TRUE
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

if len(s1) == len(s2) and s1 in (s2 + s2):
    print("TRUE")
else:
    print("FALSE")


"""
48. Remove all vowels.
Input:
S = "aeiou XYZ"

Output:
" XYZ"
"""

s = input("Enter String : ")

vowels = "aeiouAEIOU"

result = ""

for i in s:
    if i not in vowels:
        result += i

print("Result :", result)


"""
49. Replace all consonants with '*'.
Input:
S = "apple"

Output:
"a**le"
"""

s = input("Enter String : ")

vowels = "aeiouAEIOU"

result = ""

for i in s:
    if i.isalpha() and i not in vowels:
        result += "*"
    else:
        result += i

print("Result :", result)


"""
50. Remove all digits.
Input:
S = "a1b2c3"

Output:
"abc"
"""

s = input("Enter String : ")

result = ""

for i in s:
    if not i.isdigit():
        result += i

print("Result :", result)


"""
51. Extract only digits.
Input:
S = "a1b2c3"

Output:
"123"
"""

s = input("Enter String : ")

result = ""

for i in s:
    if i.isdigit():
        result += i

print("Digits :", result)


"""
52. Remove all special characters.
Input:
S = "a!@b#c"

Output:
"abc"
"""

s = input("Enter String : ")

result = ""

for i in s:
    if i.isalnum():
        result += i

print("Result :", result)


"""
53. Remove punctuation.
Input:
S = "Hello, world!"

Output:
"Hello world"
"""

s = input("Enter String : ")

punctuation = "!@#$%^&*(),.?\":{}|<>"

result = ""

for i in s:
    if i not in punctuation:
        result += i

print("Result :", result)




"""
54. Replace duplicate chars with '$'.
Input:
S = "hello"

Output:
"hel$o"
"""

s = input("Enter String : ")

seen = []
result = ""

for i in s:
    if i in seen:
        result += "$"
    else:
        result += i
        seen.append(i)

print("Result :", result)



"""
55. Reverse only vowels.
Input:
S = "hello"

Output:
"holle"
"""

s = input("Enter String : ")

vowels = "aeiouAEIOU"

vowel_list = []

for i in s:
    if i in vowels:
        vowel_list.append(i)

vowel_list.reverse()

result = ""

index = 0

for i in s:
    if i in vowels:
        result += vowel_list[index]
        index += 1
    else:
        result += i

print("Result :", result)




"""
56. Reverse only consonants.
Input:
S = "apple"

Output:
"elppa"
"""

s = input("Enter String : ")

vowels = "aeiouAEIOU"

cons = []

for i in s:
    if i.isalpha() and i not in vowels:
        cons.append(i)

cons.reverse()

result = ""

index = 0

for i in s:
    if i.isalpha() and i not in vowels:
        result += cons[index]
        index += 1
    else:
        result += i

print("Result :", result)




"""
57. Merge two strings alternatively.
Input:
S1 = "ABC"
S2 = "def"

Output:
"AdBeCf"
"""

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

result = ""

length = min(len(s1), len(s2))

for i in range(length):
    result += s1[i]
    result += s2[i]

result += s1[length:]
result += s2[length:]

print("Result :", result)




"""
58. Rotate characters left by 2 positions.
Input:
S = "abcde"

Output:
"cdeab"
"""

s = input("Enter String : ")

n = 2

result = s[n:] + s[:n]

print("Result :", result)


"""
59. Rotate characters right by 3 positions.
Input:
S = "abcde"

Output:
"cdeab"

"""

s = input("Enter String : ")

n = 3

result = s[-n:] + s[:-n]

print("Result :", result)




"""
60. Append two strings but remove adjacent duplicates.
Input:
S1 = "miss"
S2 = "issippi"

Output:
"misisipi"

"""


s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

s = s1 + s2

result = s[0]

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        result += s[i]

print("Result :", result)

