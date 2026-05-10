"""
**9. Check All Digits Are Even**
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
"""

n = int(input("Enter the number = "))
count = 0
while n>0:
    last = n%10
    n = n//10
    if last % 2 ==0:
        pass
    else:
        count += 1

if count > 0:
    print("Not All Even")
else:
    print("All Even")


