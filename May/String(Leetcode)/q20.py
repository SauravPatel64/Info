""" 
Q20. Find the lowest frequency character. 
Input: 
S = "aabbcde" 

output: 'c', 'd', 'e' (any one or all)
"""

s = input("Enter String : ")
min = 99
char =  ""
newStr = ""

for i in range(len(s)):
    count = 1
    if s[i] not in newStr:
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                count += 1
        if count < min:
            min = count
            char = s[i]
            
        newStr = newStr + s[i]   

        
print(char)
