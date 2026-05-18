"""
3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times
"""

num = input("Enter product review: ")
c = input("Enter the character to count : ")
count = 0

for ch in num:
    if ch == c:
        count = count+1
print(f"Character 'o' occurs: {count} times")