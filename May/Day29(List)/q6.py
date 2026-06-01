"""  
6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
"""

elements = list(map(int, input().strip('[]').replace(',', ' ').split()))

primes = []

for num in elements:
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

count = len(primes)
prime_sum = sum(primes)

if count > 0:
    prime_max = max(primes)
else:
    prime_max = -1

print(f"Prime IDs = {primes}")
print(f"Sum = {prime_sum}")
print(f"Max = {prime_max}")
print(f"Count = {count}")
