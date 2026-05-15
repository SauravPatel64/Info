"""
Q1.
Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
"""

feed = input("Please Enter feedback = ")

count = 0

for ch in feed:
    if ch.lower()=="a" or ch.lower()=="e" or ch.lower()=="i" or ch.lower()=="o" or ch.lower()=="u":
        count = count + 1
print(f"Output : Total vowels: {count}")