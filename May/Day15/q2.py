"""
2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5

"""
feed = input("Please Enter feedback = ")

space = 0

for ch in feed:
    if ch.isspace():
        space = space + 1
print(f"Total space: {space}")