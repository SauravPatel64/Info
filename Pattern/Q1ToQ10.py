
# Q1 *********
"""
n = int(input("Enter Number = "))
for i in  range(n):
    print("*",end="")

"""

"""
Q2

*
*
*
*
*


n = int(input("Enter Number = "))
for i in  range(n):
    print("*")
    
"""

"""
Q3
*
 *
  *
   *
    *

"""
"""

n = int(input("Enter Number = "))

for i in range(0,n):
    print(" "*i,"*")
    
"""
"""
Q4

*****
*****
*****
*****
*****

"""
"""
n = int(input("Enter numer = "))

for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
    
"""
"""
Q5

12345
12345
12345
12345
12345

"""
"""
num = int(input("Enter numer = "))

for i in range(1,num+1):
    for j in range(1,num+1):
        print(j,end="")
    print()
    
"""
"""
Q6

11111
22222
33333
44444
55555

"""

"""
num = int(input("Enter numer = "))

for i in range(1,num+1):
    for j in range(1,num+1):
        print(i,end="")
    print()

"""

"""

Q7
1
00
111
0000
11111

"""

"""
num = int(input("Enter numer = "))

for i in range(1,num+1):
    
    if i%2==0:
        for k in range(i):
            print(0,end="")
    else:
        for k in range(i):
            print(1,end="")         
    print()
    

"""

"""
Q8

*
**
***
****
*****

"""
"""

num = int(input("Enter numer = "))

for i in range(1,num+1):
    for  j in range(i):
        print("*",end="")
    print()
"""

"""      
Q9

1
12
123
1234
12345

"""

"""
num = int(input("Enter numer = "))

for i in range(1,num+1):
    for  j in range(1,i+1):
        print(j,end="")
    print()

"""


"""
Q10

1
22
333
4444
55555
"""
"""
num = int(input("Enter numer = "))

for i in range(1,num+1):
    for  j in range(1,i+1):
        print(i,end="")
    print()

"""
"""
Q11

A
AB
ABC
ABCD
ABCDE

"""
"""
num = int(input("Enter numer = "))
ch = 64
for i in range(1,num+1):
    for  j in range(1,i+1):
        print(chr(ch+j),end="")
    print()
"""
"""
Q12

a
ab
abc
abcd
abcde

"""
"""
num = int(input("Enter numer = "))
ch = 96
for i in range(1,num+1):
    for  j in range(1,i+1):
        print(chr(ch+j),end="")
    print()
 
"""

