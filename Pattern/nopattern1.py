'''1
1
23
456
78910

'''

'''
a=int(input("Enter number :"))
f=1
for i in range (a):
    print()
    for j in range (i+1):
        print(f,end='')
        f+=1
'''


'''2
1
01
101
0101
10101
'''

'''
a=int(input("Enter number :"))
for i in range (1,a+1):
    print()
    for  j in range (1,i+1):
        if (i+j)%2==1 :
            print("0",end='')
        else :
            print("1",end='')
'''



'''3
1
10
101
1010
10101
'''

'''
a=int(input("Enter number :"))
for i in range (1,a+1):
    print()
    for j in range (1,i+1):
        if j%2==1:
            print("1",end='')
        else :
            print("0",end='')
'''





'''4
1
12
1 3
1  4
12345

'''

'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if j==0:
            print("1",end='')
        elif i==j or i+1==a:
            print(j+1,end='')
        else :
            print(" ",end='')
'''




'''5
1
22
3 3
4  4
55555
'''



'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if  i==j:
            print(j+1,end='')
        elif i+1==a or j==0:
            print(i+1,end='')
        else :
            print(" ",end='')

'''









'''6
5
54
543
5432
54321
'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        print(a-j,end='')
'''





'''7
1
123
12345
1234567
123456789
'''


'''
a=int(input("Enter number :"))
for i in range (1,a+1):
    print()
    for j in range (1,i*2):
        print(j,end='')

'''









'''8
1
10
1 1
1  0
10101
'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if j==0:
            print("1",end='')
        elif i+1==a or i==j:
            if j%2==0:
                print("1",end='')
            else :
                print("0",end='')
        else :
            print(" ",end='')

'''







'''9
1
222
33333
4444444
555555555
'''


'''
a=int(input("Enter number :"))
for i in range (1,a+1):
    print()
    for j in range (1,i*2):
        print(i,end='')
'''









'''10



12345
1234
123
12
1
'''

'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        print(j+1,end='')
'''





'''11

55555
4444
333
22
1
'''


'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        print(i,end='')
'''





'''12


123456
54321
1234
321
12
1
'''

'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        if (a-i)%2==0:
            print(j+1,end='')
        else:
             print(i-j,end='')
'''







'''13


54321
5432
543
54
5
'''


'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    k=i
    for j in range (i):
        print(k-j,end='')

'''










'''14



55555
4  4
3 3
22
1
'''

'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        if i==a or j==0 or j==i-1:
            print(i,end='')
        else:
            print(" ",end='')
'''



'''15


55555
 4444
  333
   22
    1
'''

'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    for j in range (a):
        if j==a-1 or i==a or i>=a-j:
            print(i,end='')
        else :
            print(" ",end='')
'''


'''16


12345
 1234
  123
   12
    1
'''


'''

a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    h=1
    for j in range (a):
        if i==a :
            print(j+1,end='')
        elif j==a-1:
            print(i,end='')
        elif i>=a-j:
            print(h,end='')
            h=h+1
        else :
            print(" ",end='')

'''



'''17



12345
 1__4
  1_3
   12
    1
'''

'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    for j in range (a):
        if i==a :
            print(j+1,end='')
        elif j==a-1:
            print(i,end='')
        elif i==a-j:
            print("1",end='')
        elif i>a-j:
            print("_",end='')
        else :
            print(" ",end='')
'''



'''18


55555
 4__4
  3_3
   22
    1
'''


'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    for j in range (a):
        if i==a :
            print(a,end='')
        elif j==a-1:
            print(i,end='')
        elif i==a-j:
            print(i,end='')
        elif i>a-j:
            print("_",end='')
        else :
            print(" ",end='')


'''







'''19




11111
 2222
  333
   44
    5
'''

'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    h=1
    for j in range (a):
        if i<a-j:
            print(" ",end='')
        else :
            print(a+1-i,end='')
'''


'''20


    1
   12
  123
 1234
12345

'''
'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    d=1
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (1,i+2):
        print(d,end='')
        d=d+1
'''

'''21



    1 
   22
  333
 4444
55555
'''



'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    d=1
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (1,i+2):
        print(i+1,end='')
'''



'''22


    5
   44
  333
 2222
11111
'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    d=1
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (1,i+2):
        print(a-i,end='')
'''






'''23


    1
   10
  101
 1010
10101


'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    d=1
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (1,i+2):
        if k%2==1:
            print("1",end='')
        else :
            print("0",end='')
  '''







'''24

    1
   11
  1*1
 1**1
11111

'''


'''
a=int(input("Enetr number :"))
for i in range (a):
    print()
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (i+1):
        if i+1==a or k==i or k==0:
            print("1",end='')
        else :
            print("*",end='')


'''        






'''25

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    h=1
    for j in range (a):
        if j>=a-i-1:
            print(h,end=' ')
            h=h+1
        else :
            print(" ",end='')
'''


'''26



    1
   123
  12345
 1234567
123456789

'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    l=1
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (i*2+1):
        print(l,end='')
        l=l+1

'''



'''27

1
1 2
1  3
1   4
1  3
1 2
1


'''


'''
a=int(input("Enter number :"))
for i in range (a*2-1):
    print()
    if i<a:
        g=i+1
    else :
        g=(a*2-1)-i
    for j in range (g):
        if j==0:
            print("1",end='')
        elif j==g-1:
            print(g,end='')
        else :
            print(" ",end='')

'''





'''28

    1
   212
  32123
 4321234
543212345

'''
'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    m=2
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (i*2+1):
        if i>=k:
            print(i+1-k,end='')
        else :
            print(m,end='')
            m=m+1
'''








'''29



   1
  12
 123
1234
 123
  12
   1
'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (a-1-i):
        print(" ",end='')
    for k in range (i+1):
        print(k+1,end='')

for b in range (a-1):
    print()
    for c in range (b+1):
        print(" ",end='')
    for d in range (a-1-b):
        print(d+1,end='')



'''
