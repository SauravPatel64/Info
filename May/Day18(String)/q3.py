"""
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
"""

num = input("Enter commplaint: ")
count = 0

first = num[0]
if first==" ":
    count = count-1

for ch in  num:
    if ch==" ":
        count = count+1
    
print(f"Total words: {count+1}")