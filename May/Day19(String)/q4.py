"""
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop

"""

msg = input("Enter message: ")
result = ""

ls = msg.split(" ")

for i in range(0,len(ls)):
    new = ls[i]
    result = result + new[::-1] + " "

print(result)
