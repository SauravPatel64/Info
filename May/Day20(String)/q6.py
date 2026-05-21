"""
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:

```
iphone is good and iphone battery is strong
```

Word:
iphone


Output:

2 
"""

s = input("Enter Sentence : ")
word = input("Enter Word : ")
count = 0

ls = s.split()

for ch in ls:
    if word == ch:
        count = count+1

print("Output is : ", count)
