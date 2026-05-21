


s = input("Enter string = ")

s1 = ""


for i in range(len(s)):
    
    count = 0
    if s[i] not in s1:
        s1 = s1 + s[i]
        for j in range(len(s)):
            if s[i] == s[j]:
                count = count+1
                
        else:
            print(s[i]," ->",count,end=", ")


                

