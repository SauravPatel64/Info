n =  int(input("Enter number :"))

sqr = n**2

sum = 0

while (sqr>0):
    digit = sqr%10
    sum += digit 
    sqr = sqr//10

if sum == n:
    print("true")
else:
    print("false")


