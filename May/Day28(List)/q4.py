"""



4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
"""


n=int(input("Enter no. of element:"))
a=[]
for i in range(n):
    x=int(input("Enter number:"))
    a.append(x)
print(a)
s=0
count=0
l=[]
for n in a:
    x=n
    while n>0:
        a=n%10
        s=s*10+a
        n=n//10
    if x == s:
        l.append(x)
        count+=1

print("Palindromes:",l)
print("Count:",count)
l.sort()
print("Largest:",l[-1])
print("Sorted:",l)











