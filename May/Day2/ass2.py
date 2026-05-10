"""
2.
Digit Order Break Analyzer

A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

Write a program to:

Traverse the digits from left to right
Check whether each digit is greater than the previous digit
If the pattern breaks at any point, stop checking further using break
Display the position where the order breaks (1-based index)
If no break occurs, print Strictly Increasing Number

Use loops and break wherever required.

Input:
12357

Output:
Strictly Increasing Number

Input:
12342

Output:
Break at position = 4
Not Increasing Number

"""


num = int(input("Input = "))
i = 1
n = 0

while num>0:
    last = num%10
    n = n*10 + last
    num = num//10



while n >10:
    last = n%10
    temp = n//10
    lastSec = temp%10
    if lastSec > last:
        i+=1
        n = n//10

    else:
        print(f"Break at position = {i}")
        print("Not increasing Number")
        break

else:
    print("Strictly Increasing Number")


