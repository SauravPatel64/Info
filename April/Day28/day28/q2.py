'''
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''
a=int(input("Enter :"))

next=a+1


while True :
    c=0
    
    for i in range (2,next//2+1):
        if next%i==0:
            c=1 
            break
    if c==0:
        print("Next Prime =",next)
        break
    next=next+1

        

    
                 
        
    