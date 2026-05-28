# Q14

s = input("Enter String : ")
d = input("Enter String : ")

n = len(s)
m = len(d)

if not d:
    print(0)
for i in range(n-m+1):
    if s[i:i+m] == d:
        print(i)
else:
    print(-1)