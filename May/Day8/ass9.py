"""
9.
    1
   10
  101
 1010
10101

"""
n = int(input("Enter Number = "))

for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end="")
        num = 1
    for j in range(0,i+1):
        if j==1:
            print(num,end="")
        elif j%2==0:
            s = num*10
            print(s,end="")
        else:
            s = num*10+1
            print(s,end="")
    print()