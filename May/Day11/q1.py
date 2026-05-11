
"""
1) Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********
"""
n = 5
for i in range(1,n+1):
    for s in range(i,n):
        print(" ",end="")
    
    for i in range(0,i):
        if i ==1:
            print("*")
        if i>1:
            print("*",end="")
            for k in range(1,i+1):
                print(" ",end="")
            print("*")
        
