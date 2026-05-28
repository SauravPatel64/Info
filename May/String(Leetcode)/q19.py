""" 
19). Find the highest frequency character. 
S = "abracadabra" 
output:- 'a'
"""

s = input("Enter String : ")
max = 0
maxChar =  ""
newStr = ""

for i in range(len(s)-1):
    count = 1
    if s[i] not in  newStr:
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                count += 1
        if count >= max:
            max = count
            maxChar = s[i]
    
    else:
        newStr = newStr + s[i]

print(maxChar)
            
    
























