"""
Q10: 
"""
s = input("Enter String : ")
newStr = ""


for i in range(len(s)):
    if s[i] != " ": 
        newStr = s[i:]
        break
else:
    newStr = s

backStr = ""

for i in range(len(newStr) - 1, -1, -1):
    if newStr[i] != " ":
        backStr = newStr[0 : i + 1]
        break
else:
    backStr = newStr

words = backStr.split()
final_reversed = " ".join(words[::-1])

print(final_reversed)
