n =  int(input("Enter number :"))

largest = 0
while n>0:
    last =  n%10
    if largest <= last:
        largest = last
    n = n//10

print(largest)


    