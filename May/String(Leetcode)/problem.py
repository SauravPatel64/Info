"""
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
premium lock icon
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if not needle:
            return 0
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return  i
        return -1


"""
1.
Find Occurrence of a Word in a String
Product Review Analysis System
An e-commerce company wants to analyze customer reviews.
The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:
iphone is good and iphone battery is strong

Word:
iphone

Output:
2
"""
s = input("Enter Sentence : ")
word = input("Enter Word : ")
count=0
w = len(word)
new = s

for i in range(len(new)-w+1):  
    if new[i]==word[0]:
        if new[i:i+w] == word:
            count +=1
print(count)


"""
387. First Unique Character in a String
Easy
Topics
premium lock icon
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:
Input: s = "leetcode"
Output: 0

Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"
Output: -1
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i

        return -1
    





