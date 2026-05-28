
""" 
Replace occurrences of a character. 
S = "apple", Old='p', New='x' 

output :- "axxle"
"""

s= input("Enter String : ")
old = input("Enter old Character : ")
new = input("Enter the new Character to replace the old : ")

newStr = ""

for ch in s:
    if ch == old:
        newStr = newStr + new
    else:
        newStr = newStr + ch

print(newStr)