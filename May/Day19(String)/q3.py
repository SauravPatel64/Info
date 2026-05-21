"""
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy

"""

msg = input("Enter message: ")
result = ""
is_space = False

for ch in msg:
    if ch != " ":
        result = result+ch
        is_space = False
    else:
        if not is_space:
            result = result + " "
            is_space = True
            
print(f"Cleaned Message: {result}")