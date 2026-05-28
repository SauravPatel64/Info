

s = input("Ener String : ")
part = input("Enter part of a String : ")
next = ""
m = len(part)
i=0
while i<len(s)-len(part):
    if s[i] == part[0] and s[i:i+m]==part:
        i = i+len(part)
        pass
    else: 
        next = next + s[i]
        i=i+1

        
print(next)