"""
1
00
111
0000
11111
"""

n = int(input("Enter your n"))

for i in range(1,n+1):
    if i%2==0:
        while i>0:
            print(0,end="")
            i = i-1
        print()
        
    else:
        while i>0:
            print(1,end="")
            i = i-1
        print()