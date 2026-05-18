'''1
A
AB
ABC
ABCD
ABCDE
'''
'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    f=65
    for j in range (i+1):
        print(chr(f),end='')
        f=f+1
        
'''


'''2
a
ab
abc
abcd
abcde


'''
'''
a=int(input("Enter number:"))
for i in range (a):
    print()
    f=97
    for j in range (i+1):
        print(chr(f),end='')
        f=f+1

'''

'''3
A
BB
CCC
DDDD
EEEEE
'''


'''
a=int(input("Enter number:"))
for i in range (a):
    print()
    f=65+i
    for j in range (i+1):
        print(chr(f),end='')

'''

'''4
a
bc
def
ghij
klmno

'''


'''
a =int(input("Enter number :"))
g=97
for i in range(a):
    print()
    for j in range (i+1):
        print(chr(g),end='')
        g+=1
'''


'''5
A
AB
A C
A  D
ABCDE

'''

'''
a=int(input("Enter Numeber :"))
for i in range (a):
    print()
    g=65
    for j in range (i+1):
        if i+1==a :
            print(chr(g),end='')
            g+=1
        elif j==0:
            print("A",end='')
        elif i==j:
            g=g+i
            print(chr(g),end='')
        else:
            print(" ",end='' )
'''

'''
6
a
bc
d f
g  j
klmno
'''


'''
a=int(input("Enter number:"))
g=97
for i in range (a):
    print()
    for j in range (i+1):
        if i+1==a or j==0 or i==j:
            print(chr(g),end='')
        else :
            print(" ",end='')
        g=g+1   

'''



'''
7
ABCDE
ABCD
ABC
AB
A

'''

'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    h=65
    for j in range (i):
        print(chr(h),end='')
        h+=1
'''




'''8
EEEEE
DDDD
CCC
BB
A

'''
'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    g=64+i
    for j in range (i):
        print(chr(g),end='')
'''




'''9

A
BCD
EFGHI
JKLMNOP
'''


'''
a=int(input("Enter Number:"))
g=65
for i in range (1,a+1):
    print()
    for j in range (i*2-1):
        print(chr(g),end='')
        g=g+1
'''



'''10

ABCDE
A  D
A C
AB
A
'''
'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    g=65
    for j in range (a):
        if j==0 :
            print("A",end='')
        elif i==0:
            g=g+1
            print(chr(g),end='')
        elif i+1==a-j:
            g=g+j
            print(chr(g),end='')
        else :
            print(" ",end='')
'''






'''11

ABCDE
 ABCD
  ABC
   AB
    A
'''

'''
a=int(input("Enter Number :"))

for i in range (a):
    print()
    g=65
    for j in range (a):
        if i==0:
            print(chr(g+j),end='')
        elif i==j:
            print("A",end='')
        elif i<=j:
            print(chr(g+j-i),end='')
        else :
            print(" ",end='')
'''


'''12
    A 
   AB
  ABC
 ABCD
ABCDE
'''
'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    g=65
    for j in range (a):
        if j < a-i-1:
            print(" ",end='')

        else :
            print(chr(g),end='' )
            g=g+1
'''





'''13

ABCDE
A__D
A_C
AB
A
'''
'''
a=int(input("Enter number :"))
for i in range(a):
    g=65
    print()
    for j in range(a):
        if i==0:
            print(chr(g+j),end='')
        
        elif j==0:
            print("A",end='')
        elif i+1==a-j:
            print(chr(g+j),end='')
        elif j<a-i-1:
            print("_",end='')
        else :
            print(" ",end='')
'''








'''14

    A
   AB
  A_C
 A__D
ABCDE
'''


'''
a=int(input("Enter Number :"))
for i in range (a):
    print()
    g=65
    for j in range (a):
        if j+1==a:
            print(chr(g+i),end='')
        elif i+1==a-j:
            print("A",end='')
        elif i+1==a:
            print(chr(g+j),end='')
        elif j>a-i-1:
            print("_",end='')
        else :
            print(" ",end='')

'''





'''15

    A
   A B
  A B C
 A B C D
A B C D E 

'''

'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    g=65

    for j in range (a):
        if j>=a-i-1:
            print(chr(g),end=' ')
            g=g+1
         else :
            print(" ",end='')
'''

'''16

A B C D E
 A B C D
  A B C
   A B
    A

'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i):
        print(" ",end='')
    for k in range (a-i):
        print(chr(65+k),end=' ' )
'''

















'''17


    A
   B B
  C   C
 D     D
EEEEEEEEE


'''



'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range(a-i-1):
        print(" ",end='')
    for k in range (i*2+1):
        if i+1==a:
            print(chr(65+i),end='')
        elif k==0 or k==i*2:
            print(chr(65+i),end='')
        else :
            print(" ",end='')
'''



'''18


    A
   ABC
  ABCDE
 ABCDEEF
ABCDEFGHI

'''

'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (i*2+1):
        print(chr(65+k),end='')

'''