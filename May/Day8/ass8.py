"""
8.
enter n6
 654321
  65432
   6543
    654
     65
     
"""

n =  int(input("Enter Number = "))

for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(n,i-1,-1):
        print(j,end="")
    print()