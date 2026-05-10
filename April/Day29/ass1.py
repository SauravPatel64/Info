"""
1. Triple Operation Prime Verification System
A cybersecurity company generates a security score from entered access code.

Write a program to:
- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime

"""
n = int(input("Input:"))
temp = n
s = 0
reverse = 0
i = 1
while i <= n:
    a = n % 10
    s = s + a
    reverse = reverse * 10 + a
    i += 1
    n = n // 10

print("Sum of Digits = ", s)
print("Reverse = ", reverse)
difference = (reverse - temp)
print("Difference = ", difference)
f = (difference + s)
print("Final Result = ", f)
i = 0
if i <= 1:
    print("Not Prime")
else:
    for i in range(2, f):
        if f % i == 0:
            print("not Prime")
            break
    else:
        print("Prime")