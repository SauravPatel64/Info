"""
10.
enter number6
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
"""

n = int(input('Enter Number = '))

for i in range(1,n+1):
    for j in range(0,i):
        print(j,end=" ")
    print()